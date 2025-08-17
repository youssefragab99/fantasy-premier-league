# Fantasy Premier League Data Pipeline

A comprehensive data pipeline for Fantasy Premier League (FPL) data that automatically sets up a PostgreSQL database with teams, players, and historical gameweek data from 2016-17 to the current season.

## 🚀 Quick Start

**Prerequisites**: Docker and Docker Compose installed on your system.

1. **Clone the repository**:

   ```bash
   git clone https://github.com/youssefragab/fantasy-premier-league.git
   cd fantasy-premier-league
   ```

2. **Run the setup**:

   ```bash
   ./run.sh
   ```

That's it! The script will:

- Set up a PostgreSQL database
- Run all Alembic migrations
- Load current teams and players data
- Load historical gameweek data from 2016-17 to 2024-25

## 📊 What's Included

### Database Tables

- **Teams**: Premier League teams with statistics
- **Players**: Current season players with detailed stats
- **Player History**: Historical player performance data
- **Gameweek History**: Historical gameweek data for all seasons (2016-17 to 2024-25)

### Data Sources

- **FPL API**: Live teams and players data
- **GitHub Repository**: Historical data from [vaastav/Fantasy-Premier-League](https://github.com/vaastav/Fantasy-Premier-League)

## 🛠️ Development Setup

For development or if you want to control data loading manually:

```bash
./run-dev.sh
```

This starts only the database and runs migrations, skipping data loading for faster development cycles.

### Manual Data Loading

```bash
# Load teams and players
docker exec fpl-app python -m fantasy_premier_league.data_utils.data_loading --refresh

# Load historical gameweek data
docker exec fpl-app python -m fantasy_premier_league.data_utils.file_loader
```

## 🔧 Configuration

### Environment Variables

Copy `env.example` to `.env` and customize:

```env
# Database Configuration
POSTGRES_USER=fpl
POSTGRES_PASSWORD=fplpassword
POSTGRES_DB=fpldb
DB_HOST=db
DB_PORT=5433

# Data Loading Control
SKIP_DATA_LOADING=false  # Set to true to skip data loading
KEEP_RUNNING=false       # Set to true to keep container running
```

### Database Connection

Once running, connect to the database:

```bash
# Connection details
Host: localhost
Port: 5433
Database: fpldb
Username: fpl
Password: fplpassword

# Using psql
psql postgresql://fpl:fplpassword@localhost:5433/fpldb
```

## 🐳 Docker Commands

```bash
# Start everything
docker-compose up --build

# View logs
docker-compose logs -f

# Stop containers
docker-compose down

# Reset everything (including data)
docker-compose down -v && ./run.sh

# Run individual data loading scripts
docker exec fpl-app python -m fantasy_premier_league.data_utils.data_loading --help
docker exec fpl-app python -m fantasy_premier_league.data_utils.file_loader
```

## 📁 Project Structure

```
fantasy-premier-league/
├── fantasy_premier_league/
│   ├── data_utils/
│   │   ├── data_loading.py    # FPL API data loading
│   │   └── file_loader.py     # Historical data loading
│   └── database.py            # Database configuration
├── alembic/                   # Database migrations
├── scripts/
│   └── db_check.py           # Database connection checker
├── docker-compose.yml        # Docker services configuration
├── Dockerfile                # Application container
├── entrypoint.sh             # Container startup script
├── run.sh                    # Quick start script
├── run-dev.sh               # Development setup script
└── env.example              # Environment variables template
```

## 🔄 Data Updates

The pipeline loads:

- **Current Season Data**: Teams and players from the FPL API
- **Historical Data**: Gameweek data from GitHub repository (2016-17 to 2024-25)

To refresh data:

```bash
docker exec fpl-app python -m fantasy_premier_league.data_utils.data_loading --refresh
```

## 🐛 Troubleshooting

### Container Issues

```bash
# Check container status
docker-compose ps

# View detailed logs
docker-compose logs fpl-app
docker-compose logs fpl-postgres

# Restart containers
docker-compose restart
```

### Database Issues

```bash
# Test database connection
docker exec fpl-app python scripts/db_check.py

# Check if migrations ran
docker exec fpl-app alembic current

# Re-run migrations
docker exec fpl-app alembic upgrade head
```

### Data Loading Issues

```bash
# Check if data exists
docker exec -it fpl-postgres psql -U fpl -d fpldb -c "SELECT COUNT(*) FROM teams;"

# Re-run data loading with verbose output
docker exec fpl-app python -m fantasy_premier_league.data_utils.data_loading --refresh
```

## 📈 Usage Examples

Once the data is loaded, you can analyze FPL data:

```sql
-- Top scorers this season
SELECT name, total_points FROM players ORDER BY total_points DESC LIMIT 10;

-- Team statistics
SELECT name, strength, strength_attack_home FROM teams ORDER BY strength DESC;

-- Historical gameweek data (example for 2023-24)
SELECT * FROM player_gameweek_history_2023_24 LIMIT 5;
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with `./run-dev.sh`
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

- [Fantasy Premier League](https://fantasy.premierleague.com/) for the official API
- [vaastav/Fantasy-Premier-League](https://github.com/vaastav/Fantasy-Premier-League) for historical data
