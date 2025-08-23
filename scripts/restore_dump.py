#!/usr/bin/env python3
"""
Script to restore a database from a dump file using Docker.
This can be used to quickly populate a fresh database with pre-loaded data.
"""

import os
import subprocess
import sys
from pathlib import Path


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


def restore_dump(dump_file: str | None = None) -> None:
    """Restore a PostgreSQL database from a dump file using Docker."""

    # If no dump file specified, try to find the latest one
    if not dump_file:
        dump_dir = Path("database_dumps")
        if not dump_dir.exists():
            print("❌ No database_dumps directory found!")
            print("Run create_dump.py first to create a dump.")
            sys.exit(1)

        # Look for latest.sql symlink or most recent .sql file
        latest_file = dump_dir / "latest.sql"
        if latest_file.exists() and latest_file.is_symlink():
            dump_file = str(latest_file.resolve())
        else:
            # Find most recent .sql file
            sql_files = list(dump_dir.glob("*.sql"))
            if not sql_files:
                print("❌ No .sql dump files found in database_dumps/")
                print("Run create_dump.py first to create a dump.")
                sys.exit(1)

            dump_file = str(max(sql_files, key=lambda f: f.stat().st_mtime))

    # Verify the dump file exists
    if not os.path.exists(dump_file):
        print(f"❌ Dump file not found: {dump_file}")
        sys.exit(1)

    print(f"Restoring database from: {dump_file}")

    # Parse database URL to get connection details
    db_url = get_database_url()

    # Extract connection details from URL
    if db_url.startswith("postgresql://"):
        db_url = db_url[13:]

    if "@" in db_url:
        credentials, host_db = db_url.split("@", 1)
        user, password = credentials.split(":", 1)
    else:
        user = os.getenv("POSTGRES_USER", "fpl")
        password = os.getenv("POSTGRES_PASSWORD", "fplpassword")
        host_db = db_url

    if ":" in host_db:
        host_port, database = host_db.split("/", 1)
        if ":" in host_port:
            host, port = host_port.split(":", 1)
        else:
            host = host_port
            port = "5432"
    else:
        host = host_db
        port = "5432"
        database = "fpldb"

    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"Database: {database}")
    print(f"User: {user}")

    try:
        # Check if Docker containers are running
        print("Checking if Docker containers are running...")
        result = subprocess.run(
            ["docker-compose", "ps", "-q", "db"], capture_output=True, text=True, check=True
        )

        if not result.stdout.strip():
            print("❌ PostgreSQL container is not running!")
            print("Please start your containers first with: docker-compose up -d")
            sys.exit(1)

        print("✅ PostgreSQL container is running")

        # Set PGPASSWORD environment variable for password
        env = os.environ.copy()
        env["PGPASSWORD"] = password

        # First, drop and recreate the database using Docker
        print("Dropping and recreating database...")
        drop_cmd = [
            "docker",
            "exec",
            "fpl-postgres",
            "psql",
            "-h",
            "localhost",
            "-U",
            user,
            "-d",
            "postgres",  # Connect to default postgres database
            "-c",
            f'DROP DATABASE IF EXISTS "{database}";',
        ]

        subprocess.run(drop_cmd, env=env, capture_output=True, text=True, check=True)

        create_cmd = [
            "docker",
            "exec",
            "fpl-postgres",
            "psql",
            "-h",
            "localhost",
            "-U",
            user,
            "-d",
            "postgres",
            "-c",
            f'CREATE DATABASE "{database}";',
        ]

        subprocess.run(create_cmd, env=env, capture_output=True, text=True, check=True)

        # Now restore from the dump file
        print("Restoring data from dump file...")
        restore_cmd = [
            "docker",
            "exec",
            "-i",
            "fpl-postgres",
            "psql",
            "-h",
            "localhost",
            "-U",
            user,
            "-d",
            database,
        ]

        # Read the dump file and pipe it to the restore command
        with open(dump_file) as f:
            subprocess.run(
                restore_cmd, stdin=f, env=env, capture_output=True, text=True, check=True
            )

        print("✅ Database restored successfully!")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error restoring database: {e}")
        if hasattr(e, "stdout") and e.stdout:
            print(f"stdout: {e.stdout}")
        if hasattr(e, "stderr") and e.stderr:
            print(f"stderr: {e.stderr}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Restore database from a dump file")
    parser.add_argument(
        "dump_file",
        nargs="?",
        help="Path to the dump file (optional, uses latest if not specified)",
    )

    args = parser.parse_args()
    restore_dump(args.dump_file)
