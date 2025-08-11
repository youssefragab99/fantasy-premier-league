import argparse
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from threading import Lock

import requests
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
    create_engine,
)
from sqlalchemy.orm import declarative_base, sessionmaker

# --- Database Setup ---
# This should point to the same database that you are using with Alembic.
# For this example, we'll use a local SQLite database file.
DATABASE_URL = "postgresql://fpl:fplpassword@localhost:5432/fpldb"

# Create the SQLAlchemy engine and a session factory
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our SQLAlchemy models
Base = declarative_base()

# Thread lock for printing
print_lock = Lock()


# --- SQLAlchemy Models ---
# These models must match the table structures defined in your Alembic migration.


class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    short_name = Column(String(3), nullable=False)
    strength = Column(Integer)
    strength_attack_home = Column(Integer)
    strength_attack_away = Column(Integer)
    strength_defence_home = Column(Integer)
    strength_defence_away = Column(Integer)
    strength_overall_home = Column(Integer)
    strength_overall_away = Column(Integer)


class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    second_name = Column(String(100), nullable=False)
    web_name = Column(String(100), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    element_type = Column(Integer, nullable=False)  # Position
    now_cost = Column(Integer)


class PlayerGameweekHistory(Base):
    __tablename__ = "player_gameweek_history"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    gameweek = Column(Integer, nullable=False)
    season = Column(String(10), nullable=False)
    fixture_id = Column(Integer, nullable=False)
    opponent_team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    total_points = Column(Integer, nullable=False)
    was_home = Column(Boolean, nullable=False)
    kickoff_time = Column(DateTime, nullable=True)
    team_h_score = Column(Integer, nullable=True)
    team_a_score = Column(Integer, nullable=True)
    minutes = Column(Integer, nullable=False)
    goals_scored = Column(Integer, nullable=False)
    assists = Column(Integer, nullable=False)
    clean_sheets = Column(Integer, nullable=False)
    goals_conceded = Column(Integer, nullable=False)
    own_goals = Column(Integer, nullable=False)
    penalties_saved = Column(Integer, nullable=False)
    penalties_missed = Column(Integer, nullable=False)
    yellow_cards = Column(Integer, nullable=False)
    red_cards = Column(Integer, nullable=False)
    saves = Column(Integer, nullable=False)
    bonus = Column(Integer, nullable=False)
    bps = Column(Integer, nullable=False)
    influence = Column(Float, nullable=True)
    creativity = Column(Float, nullable=True)
    threat = Column(Float, nullable=True)
    ict_index = Column(Float, nullable=True)
    value = Column(Integer, nullable=True)
    selected = Column(Integer, nullable=True)
    __table_args__ = (UniqueConstraint("player_id", "gameweek", "season", name="uq_player_gameweek_season"),)


class PlayerSeasonHistory(Base):
    __tablename__ = "player_season_history"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    season_name = Column(String(10), nullable=False)
    start_cost = Column(Integer, nullable=True)
    end_cost = Column(Integer, nullable=True)
    total_points = Column(Integer, nullable=True)
    minutes = Column(Integer, nullable=True)
    goals_scored = Column(Integer, nullable=True)
    assists = Column(Integer, nullable=True)
    clean_sheets = Column(Integer, nullable=True)
    goals_conceded = Column(Integer, nullable=True)
    own_goals = Column(Integer, nullable=True)
    penalties_saved = Column(Integer, nullable=True)
    penalties_missed = Column(Integer, nullable=True)
    yellow_cards = Column(Integer, nullable=True)
    red_cards = Column(Integer, nullable=True)
    saves = Column(Integer, nullable=True)
    bonus = Column(Integer, nullable=True)
    bps = Column(Integer, nullable=True)
    influence = Column(Float, nullable=True)
    creativity = Column(Float, nullable=True)
    threat = Column(Float, nullable=True)
    ict_index = Column(Float, nullable=True)
    __table_args__ = (UniqueConstraint("player_id", "season_name", name="uq_player_season"),)


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
            existing_team = db.query(Team).filter(Team.id == team_data["id"]).first()
            if existing_team:
                continue

            new_team = Team(
                id=team_data["id"],
                name=team_data["name"],
                short_name=team_data["short_name"],
                strength=team_data["strength"],
                strength_attack_home=team_data["strength_attack_home"],
                strength_attack_away=team_data["strength_attack_away"],
                strength_defence_home=team_data["strength_defence_home"],
                strength_defence_away=team_data["strength_defence_away"],
                strength_overall_home=team_data["strength_overall_home"],
                strength_overall_away=team_data["strength_overall_away"],
            )
            db.add(new_team)

        # Commit teams to the database so players can reference them
        db.commit()
        print("Teams data loaded successfully.")

        # --- Load Players ---
        players_data = data.get("elements", [])
        print(f"Found {len(players_data)} players in the API.")

        for player_data in players_data:
            # Check if the player already exists in the database (only if not refreshing)
            if not refresh:
                existing_player = db.query(Player).filter(Player.id == player_data["id"]).first()
                if existing_player:
                    continue

            new_player = Player(
                id=player_data["id"],
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


def process_player_history(player_id: int, total_players: int, current_index: int) -> tuple[int, bool, str]:
    """
    Process a single player's history data.
    This now loads both current season gameweek data and past season summary data.

    Args:
        player_id: The ID of the player to process
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

        # Fetch detailed player data
        url = f"https://fantasy.premierleague.com/api/element-summary/{player_id}/"
        response = requests.get(url, timeout=5)

        # Skip if player data not found (e.g., transferred out of PL)
        if response.status_code != 200:
            return player_id, False, f"Could not fetch data for player {player_id}. Status: {response.status_code}"

        player_history_data = response.json()
        gw_records_added = 0
        season_records_added = 0

        # --- Load Current Season Gameweek Data ---
        gameweeks = player_history_data.get("history", [])
        for gw_data in gameweeks:
            existing_gw = (
                db.query(PlayerGameweekHistory)
                .filter_by(player_id=player_id, gameweek=gw_data["round"], season=CURRENT_SEASON)
                .first()
            )

            if not existing_gw:
                gw_model_data = {
                    key: gw_data[key] for key in PlayerGameweekHistory.__table__.columns.keys() if key in gw_data
                }
                gw_model_data.update(
                    {
                        "player_id": player_id,
                        "gameweek": gw_data["round"],
                        "season": CURRENT_SEASON,
                        "fixture_id": gw_data["fixture"],
                        "opponent_team_id": gw_data["opponent_team"],
                        "kickoff_time": datetime.fromisoformat(gw_data["kickoff_time"].replace("Z", "+00:00"))
                        if gw_data.get("kickoff_time")
                        else None,
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
                .filter_by(player_id=player_id, season_name=season_data["season_name"])
                .first()
            )

            if not existing_season:
                season_model_data = {
                    key: season_data[key] for key in PlayerSeasonHistory.__table__.columns.keys() if key in season_data
                }
                season_model_data.update(
                    {
                        "player_id": player_id,
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
        # Get all player IDs from our database
        player_ids = [p.id for p in db.query(Player.id).all()]
        total_players = len(player_ids)
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
            executor.submit(process_player_history, player_id, total_players, i): player_id
            for i, player_id in enumerate(player_ids)
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


# --- Main Execution ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load teams and players data from FPL API")
    parser.add_argument("--refresh", action="store_true", help="Delete all existing data before loading new data")

    args = parser.parse_args()

    # This will run the function when the script is executed directly
    load_teams_and_players(args.refresh)
    load_player_history()
