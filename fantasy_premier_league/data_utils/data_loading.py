import argparse

# --- Database Setup ---
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from io import StringIO
from threading import Lock
from uuid import UUID, uuid4

import pandas as pd
import requests
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

# Import the actual models - handle both script and module execution
try:
    # When imported as a module
    from ..models.player import Player
    from ..models.player_gameweek_history import (
        PlayerGameweekHistory16_17,
        PlayerGameweekHistory17_18,
        PlayerGameweekHistory18_19,
        PlayerGameweekHistory19_20,
        PlayerGameweekHistory20_21,
        PlayerGameweekHistory21_22,
        PlayerGameweekHistory22_23,
        PlayerGameweekHistory23_24,
    )
    from ..models.player_history import PlayerGameweekHistory, PlayerSeasonHistory
    from ..models.team import Team
except ImportError:
    # When run as a script
    import sys

    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    from fantasy_premier_league.models.player import Player
    from fantasy_premier_league.models.player_gameweek_history import (
        PlayerGameweekHistory16_17,
        PlayerGameweekHistory17_18,
        PlayerGameweekHistory18_19,
        PlayerGameweekHistory19_20,
        PlayerGameweekHistory20_21,
        PlayerGameweekHistory21_22,
        PlayerGameweekHistory22_23,
        PlayerGameweekHistory23_24,
    )
    from fantasy_premier_league.models.player_history import (
        PlayerGameweekHistory,
        PlayerSeasonHistory,
    )
    from fantasy_premier_league.models.team import Team

# Constants for historical seasons
HISTORICAL_SEASONS = [
    "2016_17",
    "2017_18",
    "2018_19",
    "2019_20",
    "2020_21",
    "2021_22",
    "2022_23",
    "2023_24",
]


# --- Name Conversion Functions ---


def convert_name(name: str) -> str:
    """Convert a player name to a standard format."""
    name = remove_underscore(name)
    name = remove_number(name)
    name = remove_special_characters(name)
    name = name_lower(name)
    name = remove_trailing_whitespace(name)
    return name


def remove_underscore(name: str) -> str:
    """Remove underscores from a player name."""
    return name.replace("_", " ")


def remove_number(name: str) -> str:
    """Remove numbers from a player name."""
    return re.sub(r"\d+", "", name)


def remove_special_characters(name: str) -> str:
    """Remove special characters from a player name."""
    return unidecode(name)


def name_lower(name: str) -> str:
    """Convert a player name to lowercase."""
    return name.lower()


def remove_trailing_whitespace(name: str) -> str:
    """Remove trailing whitespace from a player name."""
    return name.strip()


# --- Player Matching Functions ---
def names_from_season(season: str) -> list[str]:
    """Get all unique player names from a given season."""
    # trunk-ignore(bandit/B608)
    query = f"SELECT DISTINCT(name) FROM player_gameweek_history_{season}"

    try:
        with engine.connect() as conn:
            result = conn.execute(query)
            names = [row[0] for row in result]
        return [convert_name(name) for name in names]
    except Exception as e:
        print(f"Error getting names from season {season}: {e}")
        return []


def get_all_current_player_names() -> list[tuple[str, str]]:
    """Get all current player names and IDs."""
    query = "SELECT CONCAT(first_name, ' ', second_name) as name, id " "FROM players;"

    try:
        with engine.connect() as conn:
            result = conn.execute(query)
            players = [(row[0], str(row[1])) for row in result]
        return [(convert_name(name), player_id) for name, player_id in players]
    except Exception as e:
        print(f"Error getting current player names: {e}")
        return []


def create_all_players_table() -> None:
    """Create the all_players table if it doesn't exist."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS all_players (
        id VARCHAR(255) PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    );
    """

    try:
        with engine.connect() as conn:
            conn.execute(create_table_sql)
            conn.commit()
        print("all_players table created/verified successfully.")
    except Exception as e:
        print(f"Error creating all_players table: {e}")


def write_all_players_to_database(players: list[dict]) -> None:
    """Write players to the all_players table."""
    if not players:
        print("No players to write to database.")
        return

    try:
        # Clear existing data
        with engine.connect() as conn:
            conn.execute("DELETE FROM all_players")
            conn.commit()

        # Insert new data
        insert_sql = "INSERT INTO all_players (id, name) VALUES (%s, %s)"
        with engine.connect() as conn:
            for player in players:
                conn.execute(insert_sql, (player["id"], player["name"]))
            conn.commit()

        print(f"Successfully wrote {len(players)} players to all_players table.")
    except Exception as e:
        print(f"Error writing players to database: {e}")


def match_players_across_seasons() -> None:
    """Match players to their IDs across all seasons and populate all_players table."""
    print("\nStarting player matching across all seasons...")

    # Create the all_players table
    create_all_players_table()

    # Get all historical player names
    all_players = []
    for season in HISTORICAL_SEASONS:
        season_players = names_from_season(season)
        all_players.extend(season_players)
        print(f"Found {len(season_players)} players in season {season}")

    # Convert to set for unique names
    unique_historical_names = set(all_players)
    current_players = get_all_current_player_names()
    current_player_names = set(name for name, _ in current_players)

    # Find players who appear in historical data but not in current players
    missing_players = unique_historical_names - current_player_names

    print(f"Total historical players: {len(unique_historical_names)}")
    print(f"Current players: {len(current_player_names)}")
    print(f"Missing players needing IDs: {len(missing_players)}")

    # Create complete list of all players with IDs
    all_players_with_ids = []

    # Add current players (keep existing IDs)
    for name, player_id in current_players:
        all_players_with_ids.append({"id": player_id, "name": name})

    # Add missing historical players (generate new IDs)
    for name in missing_players:
        all_players_with_ids.append({"id": str(uuid4()), "name": name})

    print(f"Total players with IDs: {len(all_players_with_ids)}")
    print(f"Current players retained: {len(current_players)}")
    print(f"New IDs generated for missing players: {len(missing_players)}")

    # Display first few entries as example
    print("\nFirst 5 entries:")
    for i, player in enumerate(all_players_with_ids[:5]):
        print(f"{i+1}. {player}")

    # Write to database
    write_all_players_to_database(all_players_with_ids)


def get_database_url() -> str:
    """Get database URL from environment variables or defaults."""
    env_url = os.getenv("DATABASE_URL")
    if env_url:
        return env_url

    user = os.getenv("POSTGRES_USER", "fpl")
    password = os.getenv("POSTGRES_PASSWORD", "fplpassword")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5433")
    db = os.getenv("POSTGRES_DB", "fpldb")
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"


# Create the SQLAlchemy engine and a session factory
DATABASE_URL = get_database_url()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Thread lock for printing
print_lock = Lock()


# --- Data Loading Function ---


def load_teams_and_players(refresh: bool = False) -> None:
    """
    Fetches basic FPL data (teams and players) and loads it into the database.
    It checks for existing entries to avoid duplicates unless refresh is True.

    Args:
        refresh: If True, deletes all existing data before loading new data.
    """
    print("Starting data load for teams and players...")
    db = SessionLocal()

    try:
        # FPL API endpoint for general information
        url = "https://fantasy.premierleague.com/api/bootstrap-static/"
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes

        data = response.json()

        # --- Load Teams ---
        teams_data = data.get("teams", [])
        print(f"Found {len(teams_data)} teams in the API.")

        for team_data in teams_data:
            print(team_data)
            try:
                existing_team = db.query(Team).filter(Team.fpl_id == team_data["id"]).first()
                if existing_team:
                    continue

                new_team = Team(
                    fpl_id=team_data["id"],
                    name=team_data["name"],
                    short_name=team_data["short_name"],
                    code=team_data["code"],
                    strength_attack_home=team_data["strength_attack_home"],
                    strength_attack_away=team_data["strength_attack_away"],
                    strength_defence_home=team_data["strength_defence_home"],
                    strength_defence_away=team_data["strength_defence_away"],
                    strength_overall_home=team_data["strength_overall_home"],
                    strength_overall_away=team_data["strength_overall_away"],
                )
                db.add(new_team)
            except Exception as e:
                print(f"Error loading team: {e}")

        # Commit teams to the database so players can reference them
        db.commit()
        print("Teams data loaded successfully.")

        # --- Load Players ---
        players_data = data.get("elements", [])
        print(f"Found {len(players_data)} players in the API.")

        for player_data in players_data:
            # Check if the player already exists in the database (only if not refreshing)
            if not refresh:
                existing_player = (
                    db.query(Player).filter(Player.fpl_id == player_data["id"]).first()
                )
                if existing_player:
                    continue

            # Ensure UUID for id if not set by SQLAlchemy model default
            new_player = Player(
                id=uuid4(),  # Explicitly set a UUID if your model does not auto-generate
                fpl_id=player_data["id"],
                first_name=player_data["first_name"],
                second_name=player_data["second_name"],
                web_name=player_data["web_name"],
                team_id=player_data["team"],
                element_type=player_data["element_type"],
                now_cost=player_data["now_cost"],
            )
            db.add(new_player)

        # Commit players to the database
        db.commit()
        print("Players data loaded successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from FPL API: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()  # Roll back the transaction on error
    finally:
        db.close()
        print("Database session closed.")


def process_player_history(
    player_id: UUID, total_players: int, current_index: int
) -> tuple[UUID, bool, str]:
    """
    Process a single player's history data.
    This now loads both current season gameweek data and past season summary data.

    Args:
        player_id: The FPL ID of the player to process
        total_players: Total number of players being processed
        current_index: Current index of this player in the batch

    Returns:
        Tuple of (player_id, success, message)
    """
    CURRENT_SEASON = "2024-25"  # NOTE: Make this dynamic in a real application
    db = SessionLocal()

    try:
        with print_lock:
            print(f"Processing player {current_index + 1}/{total_players} (ID: {player_id})")

        # Get the player's UUID from the database using fpl_id
        player = db.query(Player).filter(Player.fpl_id == player_id).first()
        if not player:
            return (
                player_id,
                False,
                f"Player with FPL ID {player_id} not found in database",
            )

        # Fetch detailed player data
        url = f"https://fantasy.premierleague.com/api/element-summary/{player_id}/"
        response = requests.get(url, timeout=5)

        # Skip if player data not found (e.g., transferred out of PL)
        if response.status_code != 200:
            return (
                player_id,
                False,
                f"Could not fetch data for player {player_id}. Status: {response.status_code}",
            )

        player_history_data = response.json()
        gw_records_added = 0
        season_records_added = 0

        # --- Load Current Season Gameweek Data ---
        gameweeks = player_history_data.get("history", [])
        for gw_data in gameweeks:
            existing_gw = (
                db.query(PlayerGameweekHistory)
                .filter_by(player_id=player.id, gameweek=gw_data["round"], season=CURRENT_SEASON)
                .first()
            )

            if not existing_gw:
                gw_model_data = {
                    key: gw_data[key]
                    for key in PlayerGameweekHistory.__table__.columns.keys()
                    if key in gw_data
                }
                gw_model_data.update(
                    {
                        "id": uuid4(),  # Ensure UUID for id
                        "player_id": player.id,
                        "gameweek": gw_data["round"],
                        "season": CURRENT_SEASON,
                        "fixture_id": gw_data["fixture"],
                        "opponent_team_id": gw_data["opponent_team"],
                        "kickoff_time": (
                            datetime.fromisoformat(gw_data["kickoff_time"].replace("Z", "+00:00"))
                            if gw_data.get("kickoff_time")
                            else None
                        ),
                        "influence": float(gw_data["influence"]),
                        "creativity": float(gw_data["creativity"]),
                        "threat": float(gw_data["threat"]),
                        "ict_index": float(gw_data["ict_index"]),
                    }
                )
                db.add(PlayerGameweekHistory(**gw_model_data))
                gw_records_added += 1

        # --- Load Past Season Summary Data ---
        past_seasons = player_history_data.get("history_past", [])
        for season_data in past_seasons:
            existing_season = (
                db.query(PlayerSeasonHistory)
                .filter_by(player_id=player.id, season_name=season_data["season_name"])
                .first()
            )

            if not existing_season:
                season_model_data = {
                    key: season_data[key]
                    for key in PlayerSeasonHistory.__table__.columns.keys()
                    if key in season_data
                }
                season_model_data.update(
                    {
                        "id": uuid4(),  # Ensure UUID for id
                        "player_id": player.id,
                        "influence": float(season_data["influence"]),
                        "creativity": float(season_data["creativity"]),
                        "threat": float(season_data["threat"]),
                        "ict_index": float(season_data["ict_index"]),
                    }
                )
                db.add(PlayerSeasonHistory(**season_model_data))
                season_records_added += 1
        # Commit after processing all data for this player
        db.commit()

        # Be kind to the API - add a small delay
        time.sleep(0.5)

        return (
            player_id,
            True,
            f"Successfully processed {gw_records_added} gameweek records and {season_records_added} season records",
        )

    except requests.exceptions.RequestException as e:
        db.rollback()
        return player_id, False, f"Request error: {e}"
    except Exception as e:
        db.rollback()
        return player_id, False, f"Error processing player: {e}"
    finally:
        db.close()


def load_player_history() -> None:
    """
    Fetches detailed history for each player and loads it into the database.
    This now loads both current season gameweek data and past season summary data.
    Uses concurrent processing with 32 threads.
    """
    print("\nStarting data load for player history...")
    db = SessionLocal()

    try:
        # Get all player FPL IDs from our database
        player_fpl_ids = [p.fpl_id for p in db.query(Player.fpl_id).all()]
        total_players = len(player_fpl_ids)
        print(f"Found {total_players} players in the database to process.")

    except Exception as e:
        print(f"Error getting player IDs: {e}")
        db.close()
        return
    finally:
        db.close()

    # Process players in parallel using ThreadPoolExecutor
    successful_count = 0
    failed_count = 0

    with ThreadPoolExecutor(max_workers=32) as executor:
        # Submit all tasks
        future_to_player = {
            executor.submit(process_player_history, player_fpl_id, total_players, i): player_fpl_id
            for i, player_fpl_id in enumerate(player_fpl_ids)
        }

        # Process completed tasks
        for future in as_completed(future_to_player):
            player_id, success, message = future.result()

            if success:
                successful_count += 1
            else:
                failed_count += 1
                with print_lock:
                    print(f"  - {message}")

    print("\nPlayer history loading completed.")
    print(f"Successfully processed: {successful_count} players")
    print(f"Failed to process: {failed_count} players")


def load_historical_gameweek_data_from_github() -> None:
    """
    NEW: Loads detailed gameweek-by-gameweek data for past seasons
    from the vaastav/Fantasy-Premier-League GitHub repository into
    individual season-specific tables.
    """
    print("\nStarting data load for historical gameweek data from GitHub...")

    # List of past seasons and their corresponding model classes
    PAST_SEASONS = {
        "2016-17": PlayerGameweekHistory16_17,
        "2017-18": PlayerGameweekHistory17_18,
        "2018-19": PlayerGameweekHistory18_19,
        "2019-20": PlayerGameweekHistory19_20,
        "2020-21": PlayerGameweekHistory20_21,
        "2021-22": PlayerGameweekHistory21_22,
        "2022-23": PlayerGameweekHistory22_23,
        "2023-24": PlayerGameweekHistory23_24,
    }

    total_records_added = 0
    total_records_skipped = 0
    total_errors = 0

    for season, model_class in PAST_SEASONS.items():
        print(f"Processing season: {season}")
        db = SessionLocal()
        season_records_added = 0
        season_records_skipped = 0
        season_errors = 0

        try:
            base_url = "https://raw.githubusercontent.com/vaastav/"
            url = f"{base_url}Fantasy-Premier-League/master/data/{season}/gws/merged_gw.csv"

            # Fetch the CSV content with proper encoding handling
            df = _fetch_csv_data(url, season)
            if df is None:
                continue

            # Rename columns to match our database schema
            df.rename(
                columns={"GW": "round"},
                inplace=True,
            )

            print(f"  - Found {len(df)} records in CSV")

            for index, row in df.iterrows():
                try:
                    # Skip records with null opponent_team_id
                    if _should_skip_record(row):
                        season_records_skipped += 1
                        continue

                    # Process the row data
                    model_data = _process_row_data(row, model_class, season)
                    if model_data is None:
                        season_records_skipped += 1
                        continue

                    # Try to insert the record
                    success = _insert_record(db, model_class, model_data, index)
                    if success == "added":
                        season_records_added += 1
                    elif success == "skipped":
                        season_records_skipped += 1
                    else:
                        season_errors += 1

                except Exception as e:
                    print(f"    - Error processing row {index}: {e}")
                    season_errors += 1
                    continue

            print(
                f"  - Season {season} completed: "
                f"{season_records_added} added, "
                f"{season_records_skipped} skipped, "
                f"{season_errors} errors"
            )

            total_records_added += season_records_added
            total_records_skipped += season_records_skipped
            total_errors += season_errors

        except Exception as e:
            print(f"  - Fatal error processing season {season}: {e}")
            total_errors += 1
        finally:
            db.close()

    print("\nHistorical data loading completed:")
    print(f"  - Total records added: {total_records_added}")
    print(f"  - Total records skipped: {total_records_skipped}")
    print(f"  - Total errors: {total_errors}")
    print("Database sessions closed.")


def _fetch_csv_data(url: str, season: str) -> pd.DataFrame | None:
    """Fetch and decode CSV data from URL."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # Try different encodings to decode the content
        encodings = ["utf-8", "latin1", "iso-8859-1", "cp1252", "windows-1252"]

        for encoding in encodings:
            try:
                content = response.content.decode(encoding)
                df = pd.read_csv(StringIO(content))
                print(f"  - Successfully decoded with {encoding} encoding")
                return df
            except (UnicodeDecodeError, pd.errors.ParserError) as e:
                print(f"  - Failed to decode with {encoding}: {e}")
                continue

        raise Exception("Could not decode CSV with any supported encoding")

    except requests.exceptions.RequestException as e:
        print(f"  - Could not fetch data for season {season}. " f"Network error: {e}")
        return None
    except Exception as e:
        print(f"  - Could not process data for season {season}. Error: {e}")
        return None


def _should_skip_record(row: pd.Series) -> bool:
    """Check if record should be skipped."""
    return pd.isna(row.get("opponent_team")) or row.get("opponent_team") is None


def _process_row_data(row: pd.Series, model_class: type, season: str) -> dict | None:
    """Process row data into model format."""
    gw_data = row.to_dict()

    # Ensure all required columns exist, providing defaults if not
    for col in model_class.__table__.columns:
        if col.name not in gw_data:
            gw_data[col.name] = None

    # Convert kickoff_time to datetime object
    if pd.notna(gw_data.get("kickoff_time")):
        try:
            kickoff_str = str(gw_data["kickoff_time"]).replace("Z", "+00:00")
            gw_data["kickoff_time"] = datetime.fromisoformat(kickoff_str)
        except (ValueError, TypeError):
            gw_data["kickoff_time"] = None
    else:
        gw_data["kickoff_time"] = None

    gw_data["season"] = season

    # Drop the id that is in the table model, if present
    if "id" in gw_data:
        gw_data.pop("id")

    # Filter only for columns that exist in the table model
    model_data = {
        key.name: gw_data[key.name] for key in model_class.__table__.columns if key.name in gw_data
    }

    # Ensure UUID for id
    model_data["id"] = uuid4()

    return model_data


def _insert_record(db, model_class: type, model_data: dict, index: int) -> str:
    """Insert record into database. Returns 'added', 'skipped', or 'error'."""
    try:
        db.add(model_class(**model_data))
        db.commit()
        return "added"

    except IntegrityError as e:
        db.rollback()
        if "duplicate key value violates unique constraint" in str(e).lower() or (
            "null value in column" in str(e).lower()
            and "violates not-null constraint" in str(e).lower()
        ):
            return "skipped"
        else:
            print(f"    - Integrity error for row {index}: {e}")
            return "error"
    except Exception as e:
        db.rollback()
        print(f"    - Unexpected error for row {index}: {e}")
        return "error"


# --- Main Execution ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load teams and players data from FPL API")
    parser.add_argument(
        "--refresh", action="store_true", help="Delete all existing data before loading new data"
    )

    args = parser.parse_args()

    # Load teams and players data
    # print("Loading teams and players data...")
    # load_teams_and_players(args.refresh)

    # Load player history data
    # print("Loading player history data...")
    # load_player_history()

    # # Load historical gameweek data
    print("Loading historical gameweek data from GitHub...")
    load_historical_gameweek_data_from_github()

    # Match players across seasons
    match_players_across_seasons()
