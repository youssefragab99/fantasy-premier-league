#!/bin/bash

set -e

echo "⚽️ Fantasy Premier League Data Pipeline Setup"
echo "============================================="

# Check if fast mode is enabled
if [ "$FAST_MODE" = "true" ]; then
    echo "🚀 FAST MODE ENABLED - Skipping data loading for faster startup!"
    echo "   This will use existing data or database dumps if available."
    echo ""
fi

# Check if .env exists, if not copy from example
if [ ! -f .env ]; then
    echo "📋 Creating .env file from example..."
    cp env.example .env
    echo "✅ .env file created. You can edit it to customize database settings."
fi

echo "🐳 Starting Docker containers..."
if [ "$FAST_MODE" = "true" ]; then
    echo "This will:"
    echo "  1. Start PostgreSQL database"
    echo "  2. Run Alembic migrations"
    echo "  3. Skip data loading (using existing data)"
    echo ""
    echo "💡 Fast mode: Data will be loaded from database dumps or persistent volumes"
else
    echo "This will:"
    echo "  1. Start PostgreSQL database"
    echo "  2. Run Alembic migrations"
    echo "  3. Load teams and players data"
    echo "  4. Load historical gameweek data"
    echo ""
    echo "💡 Normal mode: Fresh data will be downloaded from FPL APIs"
fi

# Build and start containers
docker-compose up --build

echo ""
if [ "$FAST_MODE" = "true" ]; then
    echo "🎉 Fast startup complete! Your Fantasy Premier League database is ready."
    echo "   Data loaded from existing sources (no API calls made)."
else
    echo "🎉 Setup complete! Your Fantasy Premier League database is ready."
    echo "   Fresh data has been downloaded and loaded."
fi
echo ""
echo "📊 Database contains:"
echo "  - Teams and current season players"
echo "  - Player statistics and history"
echo "  - Historical gameweek data from 2016-17 to 2024-25"
echo ""
echo "🔗 Database connection:"
echo "  Host: localhost"
echo "  Port: 5433"
echo "  Database: fpldb"
echo "  Username: fpl"
echo "  Password: fplpassword"
echo ""
echo "💡 Quick commands:"
echo "  - View logs: docker-compose logs -f"
echo "  - Stop containers: docker-compose down"
echo "  - Restart with fresh data: docker-compose down -v && ./run.sh"
echo "  - Access database: psql postgresql://fpl:fplpassword@localhost:5433/fpldb"
echo ""
echo "🚀 Fast mode commands:"
echo "  - Start in fast mode: FAST_MODE=true ./run.sh"
echo "  - Export for session: export FAST_MODE=true && ./run.sh"
echo "  - Create database dump: python scripts/create_dump.py"
echo "  - Restore from dump: python scripts/restore_dump.py"