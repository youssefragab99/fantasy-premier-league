#!/bin/bash

set -e

echo "🛠️  Fantasy Premier League Development Setup"
echo "============================================"

# Check if .env exists, if not copy from example
if [ ! -f .env ]; then
    echo "📋 Creating .env file from example..."
    cp env.example .env
fi

echo "🐳 Starting Docker containers in development mode..."
echo "This will:"
echo "  1. Start PostgreSQL database only"
echo "  2. Run migrations"
echo "  3. Skip data loading for faster development"
echo ""

# Set development environment variables
export SKIP_DATA_LOADING=true
export MOUNT_MODE=rw

# Build and start containers
docker-compose up --build

echo ""
echo "🎉 Development setup complete!"
echo ""
echo "💻 Development mode features:"
echo "  - Data loading skipped for faster startup"
echo "  - Code mounted as volume for live editing"
echo "  - Database ready for custom data loading"
echo ""
echo "🔗 Database connection:"
echo "  Host: localhost"
echo "  Port: 5433"
echo "  Database: fpldb"
echo "  Username: fpl"
echo "  Password: fplpassword"
echo ""
echo "📝 To load data manually:"
echo "  docker exec fpl-app python -m fantasy_premier_league.data_utils.data_loading --refresh"
echo "  docker exec fpl-app python -m fantasy_premier_league.data_utils.file_loader"