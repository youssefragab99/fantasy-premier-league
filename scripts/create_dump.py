#!/usr/bin/env python3
"""
Script to create a database dump for faster Docker container startup.
This creates a SQL dump that can be automatically loaded when the PostgreSQL container starts.
"""

import os
import subprocess
import sys
from datetime import datetime


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


def create_dump() -> str:
    """Create a PostgreSQL dump of the current database using Docker."""

    # Create database_dumps directory if it doesn't exist
    dump_dir = "database_dumps"
    os.makedirs(dump_dir, exist_ok=True)

    # Generate timestamp for the dump file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dump_file = f"{dump_dir}/fpl_dump_{timestamp}.sql"

    # Parse database URL to get connection details
    db_url = get_database_url()

    # Extract connection details from URL
    # Format: postgresql://user:password@host:port/db
    if db_url.startswith("postgresql://"):
        db_url = db_url[13:]  # Remove postgresql://

    # Split into credentials and host/db
    if "@" in db_url:
        credentials, host_db = db_url.split("@", 1)
        user, password = credentials.split(":", 1)
    else:
        user = os.getenv("POSTGRES_USER", "fpl")
        password = os.getenv("POSTGRES_PASSWORD", "fplpassword")
        host_db = db_url

    # Split host_db into host:port and database
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

    print("Creating database dump...")
    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"Database: {database}")
    print(f"User: {user}")
    print(f"Dump file: {dump_file}")

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

        # Create the dump using Docker exec
        print("Creating database dump using Docker...")

        # Use docker exec to run pg_dump inside the container
        cmd = [
            "docker",
            "exec",
            "fpl-postgres",  # Container name from docker-compose.yml
            "pg_dump",
            "-h",
            "localhost",  # Inside container, use localhost
            "-U",
            user,
            "-d",
            database,
            "--clean",  # Include DROP commands
            "--if-exists",  # Use IF EXISTS with DROP
            "--create",  # Include CREATE DATABASE command
            "--no-owner",  # Don't set ownership
            "--no-privileges",  # Don't set privileges
        ]

        print(f"Running command: {' '.join(cmd)}")

        # Run the command and capture output
        with open(dump_file, "w") as f:
            result = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, text=True, check=True)

        # Check if file was created and has content
        if os.path.exists(dump_file) and os.path.getsize(dump_file) > 0:
            print(f"✅ Database dump created successfully: {dump_file}")
            print(f"File size: {os.path.getsize(dump_file) / (1024*1024):.2f} MB")

            # Also create a latest.sql file for easy reference
            latest_file = f"{dump_dir}/latest.sql"
            if os.path.exists(latest_file):
                os.remove(latest_file)
            os.symlink(os.path.basename(dump_file), latest_file)
            print(f"✅ Created symlink: {latest_file}")

            return dump_file
        else:
            print("❌ Dump file was not created or is empty")
            sys.exit(1)

    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating dump: {e}")
        if hasattr(e, "stderr") and e.stderr:
            print(f"stderr: {e.stderr}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    create_dump()
