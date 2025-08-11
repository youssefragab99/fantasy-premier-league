import argparse

import requests
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
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
        # If refresh is True, delete all existing data
        if refresh:
            print("Refresh mode enabled. Deleting all existing data...")
            db.query(Player).delete()
            db.query(Team).delete()
            db.commit()
            print("Existing data deleted successfully.")

        # FPL API endpoint for general information
        url = "https://fantasy.premierleague.com/api/bootstrap-static/"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        data = response.json()

        # --- Load Teams ---
        teams_data = data.get("teams", [])
        print(f"Found {len(teams_data)} teams in the API.")

        for team_data in teams_data:
            # Check if the team already exists in the database (only if not refreshing)
            if not refresh:
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


# --- Main Execution ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load teams and players data from FPL API")
    parser.add_argument(
        "--refresh", 
        action="store_true", 
        help="Delete all existing data before loading new data"
    )
    
    args = parser.parse_args()
    
    # This will run the function when the script is executed directly
    load_teams_and_players(refresh=args.refresh)
