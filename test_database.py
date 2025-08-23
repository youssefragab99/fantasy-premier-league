#!/usr/bin/env python3
"""
Simple test script to verify database modules can be imported.
"""


def test_imports():
    """Test that all database modules can be imported."""
    try:
        print("Testing database imports...")

        # Test database package imports
        from fantasy_premier_league.database import (
            DatabaseSession,
            get_db_session,
            get_psycopg2_connection,
        )

        print("✓ Database package imports successful")

        # Test models imports
        from fantasy_premier_league.models import Base, Player, Team

        print("✓ Models imports successful")

        # Test database utilities
        from fantasy_premier_league.database.utils import DatabaseManager, execute_raw_sql

        print("✓ Database utilities imports successful")

        print("\nAll imports successful! Database structure is working.")
        return True

    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    test_imports()
