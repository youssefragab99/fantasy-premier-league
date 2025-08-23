#!/usr/bin/env python3
"""
Example script demonstrating database usage for Fantasy Premier League.

This script shows how to use the database modules for:
- Connecting to the database
- Using SQLAlchemy ORM models
- Direct psycopg2 operations
- Common database operations
"""

import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from fantasy_premier_league.database import (
    DatabaseSession,
    execute_query,
    get_db_session,
    get_psycopg2_connection,
)
from fantasy_premier_league.database.utils import DatabaseManager, execute_raw_sql
from fantasy_premier_league.models import Player, Team


def example_orm_usage():
    """Demonstrate SQLAlchemy ORM usage."""
    print("=== SQLAlchemy ORM Examples ===")

    # Example 1: Using the context manager
    with get_db_session() as session:
        # Get all teams
        teams = session.query(Team).all()
        print(f"Found {len(teams)} teams")

        # Get players with their team information
        players = session.query(Player).join(Team).limit(5).all()
        for player in players:
            print(f"Player: {player.name} - Team: {player.team.name}")

    # Example 2: Using the DatabaseSession class
    with DatabaseSession() as session:
        # Create a new team
        new_team = Team(name="Example FC", short_name="EXM", code=999)
        session.add(new_team)
        # Session will auto-commit on exit if no exception occurs

    print("ORM examples completed successfully!")


def example_direct_psycopg2():
    """Demonstrate direct psycopg2 usage."""
    print("\n=== Direct psycopg2 Examples ===")

    # Example 1: Using the context manager
    with get_psycopg2_connection() as conn:
        with conn.cursor() as cur:
            # Get table names
            cur.execute(
                """
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name
            """
            )
            tables = cur.fetchall()
            print(f"Database tables: {[table[0] for table in tables]}")

    # Example 2: Using utility functions
    # Get all players
    players = execute_query("SELECT name, position FROM players LIMIT 5")
    print(f"Sample players: {players}")

    # Get table information
    table_info = execute_query(
        """
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = 'players'
        ORDER BY ordinal_position
    """
    )
    print(f"Players table columns: {table_info}")

    print("Direct psycopg2 examples completed successfully!")


def example_database_manager():
    """Demonstrate DatabaseManager usage."""
    print("\n=== DatabaseManager Examples ===")

    # Create managers for different models
    player_manager = DatabaseManager(Player)
    team_manager = DatabaseManager(Team)

    with get_db_session() as session:
        # Get all teams
        teams = team_manager.get_all(session)
        print(f"Total teams: {len(teams)}")

        # Get players by position
        defenders = player_manager.filter_by(session, position="DEF")
        print(f"Total defenders: {len(defenders)}")

        # Get player count
        total_players = player_manager.count(session)
        print(f"Total players: {total_players}")

    print("DatabaseManager examples completed successfully!")


def example_raw_sql():
    """Demonstrate raw SQL execution."""
    print("\n=== Raw SQL Examples ===")

    # Execute a complex query
    results = execute_raw_sql(
        """
        SELECT 
            p.name as player_name,
            t.name as team_name,
            p.position,
            COUNT(ph.id) as gameweek_appearances
        FROM players p
        JOIN teams t ON p.team_id = t.id
        LEFT JOIN player_gameweek_history ph ON p.id = ph.player_id
        GROUP BY p.id, p.name, t.name, p.position
        ORDER BY gameweek_appearances DESC
        LIMIT 10
    """
    )

    print("Top 10 players by gameweek appearances:")
    for result in results:
        print(
            f"{result['player_name']} ({result['team_name']}) - "
            f"{result['position']} - {result['gameweek_appearances']} appearances"
        )

    print("Raw SQL examples completed successfully!")


def example_bulk_operations():
    """Demonstrate bulk database operations."""
    print("\n=== Bulk Operations Examples ===")


    # Example bulk insert (commented out to avoid actual insertion)
    """
    new_players = [
        {"name": "John Doe", "team_id": 1, "position": "MID", "is_active": True},
        {"name": "Jane Smith", "team_id": 1, "position": "FWD", "is_active": True},
    ]
    
    with get_db_session() as session:
        players = bulk_insert(Player, new_players)
        print(f"Inserted {len(players)} new players")
    """

    print("Bulk operations examples completed successfully!")


def main():
    """Run all database examples."""
    print("Fantasy Premier League Database Examples")
    print("=" * 50)

    try:
        # Test database connection first
        with get_db_session() as session:
            # Simple query to test connection
            result = session.execute("SELECT 1 as test").fetchone()
            if result and result[0] == 1:
                print("✓ Database connection successful!")
            else:
                print("✗ Database connection failed!")
                return

        # Run examples
        example_orm_usage()
        example_direct_psycopg2()
        example_database_manager()
        example_raw_sql()
        example_bulk_operations()

        print("\n" + "=" * 50)
        print("All examples completed successfully!")

    except Exception as e:
        print(f"\n✗ Error running examples: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
