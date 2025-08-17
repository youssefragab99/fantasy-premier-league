#!/bin/bash

set -e

echo "⚽️ Fantasy Premier League Data Pipeline Setup"
echo "============================================="

# Check if .env exists, if not copy from example
if [ ! -f .env ]; then
    echo "📋 Creating .env file from example..."
    cp env.example .env
    echo "✅ .env file created. You can edit it to customize database settings."
fi

echo "🐳 Starting Docker containers..."
echo "This will:"
echo "  1. Start PostgreSQL database"
echo "  2. Run Alembic migrations"
echo "  3. Load teams and players data"
echo "  4. Load historical gameweek data"
echo ""

# Build and start containers
docker-compose up --build

echo ""
echo "🎉 Setup complete! Your Fantasy Premier League database is ready."
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