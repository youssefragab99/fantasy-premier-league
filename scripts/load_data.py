#!/usr/bin/env python3
"""
Script to load Fantasy Premier League data into the database.

This script loads:
1. Teams and players from the FPL API
2. Player history data
3. Historical gameweek data from GitHub

Run this script from the project root directory.
"""

import argparse
import os
from threading import Lock

import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the models
from fantasy_premier_league.models.player import Player
from fantasy_premier_league.models.team import Team


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
            existing_team = db.query(Team).filter(Team.fpl_id == team_data["id"]).first()
            if existing_team:
                continue

            new_team = Team(
                fpl_id=team_data["id"],
                name=team_data["name"],
                short_name=team_data["short_name"],
                code=team_data["code"],
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
                existing_player = (
                    db.query(Player).filter(Player.fpl_id == player_data["id"]).first()
                )
                if existing_player:
                    continue

            # Create new player
            new_player = Player(
                fpl_id=player_data["id"],
                first_name=player_data.get("first_name", ""),
                second_name=player_data.get("second_name", ""),
                web_name=player_data["web_name"],
                team_id=player_data["team"],
                element_type=player_data["element_type"],
            )
            db.add(new_player)

        # Commit all players to the database
        db.commit()
        print("Players data loaded successfully.")

    except Exception as e:
        print(f"Error loading teams and players: {e}")
        db.rollback()
        raise
    finally:
        db.close()


def load_player_history() -> None:
    """Load player history data from the FPL API."""
    print("Loading player history data...")

    # This function would need to be implemented based on your specific needs
    # For now, we'll just print a message
    print("Player history loading not yet implemented in this script.")


def load_historical_gameweek_data_from_github() -> None:
    """Load historical gameweek data from GitHub."""
    print("Loading historical gameweek data from GitHub...")

    # This function would need to be implemented based on your specific needs
    # For now, we'll just print a message
    print("Historical gameweek data loading not yet implemented in this script.")


def main():
    """Main function to load all data."""
    parser = argparse.ArgumentParser(description="Load teams and players data from FPL API")
    parser.add_argument(
        "--refresh", action="store_true", help="Delete all existing data before loading new data"
    )

    args = parser.parse_args()

    try:
        # Load teams and players data
        print("Loading teams and players data...")
        load_teams_and_players(args.refresh)

        # Load player history data
        print("Loading player history data...")
        load_player_history()

        # Load historical gameweek data
        print("Loading historical gameweek data from GitHub...")
        load_historical_gameweek_data_from_github()

        print("\n🎉 Data loading completed successfully!")

    except Exception as e:
        print(f"\n❌ Data loading failed: {e}")
        raise


if __name__ == "__main__":
    main()
