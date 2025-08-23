#!/bin/bash

set -e

echo "Starting Fantasy Premier League data pipeline (Fast Mode)..."

# Wait for the database to be ready
echo "Waiting for database to be ready..."
python scripts/db_check.py

# Run Alembic migrations
echo "Running Alembic migrations..."
alembic upgrade head

# Check if we should use fast mode (skip data loading)
if [ "$FAST_MODE" = "true" ] || [ "$SKIP_DATA_LOADING" = "true" ]; then
    echo "Fast mode enabled - skipping data loading"
    echo "Database is ready with existing data."
    
    if [ "$KEEP_RUNNING" = "true" ]; then
        echo "Keeping container running (KEEP_RUNNING=true)..."
        tail -f /dev/null
    fi
    exit 0
fi

# Check if database already has data
echo "Checking if database already contains data..."
python -c "
import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

try:
    engine = create_engine(os.environ['DATABASE_URL'])
    with engine.connect() as conn:
        result = conn.execute(text('SELECT COUNT(*) FROM teams'))
        team_count = result.scalar()
        result = conn.execute(text('SELECT COUNT(*) FROM players'))
        player_count = result.scalar()
        
        if team_count > 0 and player_count > 0:
            print(f'Database already contains {team_count} teams and {player_count} players')
            exit(0)  # Data exists, skip loading
        else:
            print('Database is empty, will load data')
            exit(1)  # No data, need to load
except Exception as e:
    print(f'Error checking database: {e}')
    exit(1)  # Error, assume we need to load data
"

if [ $? -eq 0 ]; then
    echo "✅ Database already contains data - skipping data loading"
    echo "Fantasy Premier League database is ready to use."
    
    if [ "$KEEP_RUNNING" = "true" ]; then
        echo "Keeping container running (KEEP_RUNNING=true)..."
        tail -f /dev/null
    fi
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