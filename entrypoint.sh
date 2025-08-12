#!/bin/bash

set -e

echo "Starting Fantasy Premier League data pipeline..."

# Wait for the database to be ready
echo "Waiting for database to be ready..."
python scripts/db_check.py

# Run Alembic migrations
echo "Running Alembic migrations..."
alembic upgrade head

# Check if data loading should be skipped (for development)
if [ "$SKIP_DATA_LOADING" = "true" ]; then
    echo "Skipping data loading (SKIP_DATA_LOADING=true)"
    echo "Setup complete. Database is ready."
    exit 0
fi

# Load teams and players data
echo "Loading teams and players data..."
python -m fantasy_premier_league.data_utils.data_loading --refresh

# Load historical gameweek data
echo "Loading historical gameweek data..."
python -m fantasy_premier_league.data_utils.file_loader

echo "Data pipeline completed successfully!"
echo "Fantasy Premier League database is fully loaded and ready to use."

# Keep container running if needed
if [ "$KEEP_RUNNING" = "true" ]; then
    echo "Keeping container running (KEEP_RUNNING=true)..."
    tail -f /dev/null
fi