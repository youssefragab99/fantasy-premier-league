# Database Module Documentation

This directory contains the database infrastructure for the Fantasy Premier League application, providing both SQLAlchemy ORM and direct psycopg2 connection capabilities.

## Overview

The database module is designed to be modular and easy to use across different parts of the application. It provides:

- **Configuration Management**: Database connection configuration and URL construction
- **Session Management**: SQLAlchemy session handling with automatic transaction management
- **Direct Connections**: Raw psycopg2 connections for complex queries and bulk operations
- **Utility Functions**: Common database operations and helper functions
- **ORM Models**: SQLAlchemy models for all database tables

## Module Structure

```
fantasy_premier_league/database/
├── __init__.py          # Package initialization and exports
├── config.py            # Database configuration and connection setup
├── session.py           # Session management and context managers
├── connection.py        # Direct psycopg2 connection handling
├── utils.py             # Database utilities and helper functions
└── README.md            # This documentation file
```

## Quick Start

### Basic Usage

```python
from fantasy_premier_league.database import get_db_session, DatabaseSession

# Using the context manager
with get_db_session() as session:
    # Your database operations here
    players = session.query(Player).all()
    # Session automatically commits on success, rolls back on error

# Using the DatabaseSession class
with DatabaseSession() as session:
    new_player = Player(name="John Doe", position="MID")
    session.add(new_player)
    # Auto-commit on success, auto-rollback on error
```

### Direct psycopg2 Usage

```python
from fantasy_premier_league.database import get_psycopg2_connection, execute_query

# Using the context manager
with get_psycopg2_connection() as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM players LIMIT 5")
        results = cur.fetchall()

# Using utility functions
players = execute_query("SELECT name, position FROM players LIMIT 5")
```

## Configuration

The database configuration is loaded from `config.yaml` in the project root:

```yaml
db:
  username: fpl
  password: fplpassword
  database: fpldb
  host: localhost
  port: 5433
```

You can also override the configuration using the `DATABASE_URL` environment variable:

```bash
export DATABASE_URL="postgresql+psycopg2://user:pass@host:port/db"
```

## Session Management

### get_db_session()

A context manager that provides automatic transaction management:

```python
from fantasy_premier_league.database import get_db_session

with get_db_session() as session:
    # Your database operations
    result = session.query(Player).filter_by(position="MID").all()
    # Session commits on success, rolls back on error
```

### DatabaseSession Class

A class-based session manager with additional features:

```python
from fantasy_premier_league.database import DatabaseSession

# Basic usage
with DatabaseSession() as session:
    # Your operations here
    pass

# Using the execute_query method
db_session = DatabaseSession()
result = db_session.execute_query(lambda s: s.query(Player).all())
```

## Direct Database Operations

### Raw SQL Execution

```python
from fantasy_premier_league.database.utils import execute_raw_sql

# Execute a complex query
results = execute_raw_sql("""
    SELECT p.name, t.name as team_name
    FROM players p
    JOIN teams t ON p.team_id = t.id
    WHERE p.position = %(position)s
""", {"position": "MID"})

# Results are returned as dictionaries
for row in results:
    print(f"{row['name']} - {row['team_name']}")
```

### Bulk Operations

```python
from fantasy_premier_league.database.utils import bulk_insert, bulk_update

# Bulk insert
new_players = [
    {"name": "Player 1", "position": "MID"},
    {"name": "Player 2", "position": "FWD"},
]
players = bulk_insert(Player, new_players)

# Bulk update
updates = [
    {"id": 1, "position": "DEF"},
    {"id": 2, "position": "MID"},
]
updated_count = bulk_update(Player, updates)
```

## Database Manager

The `DatabaseManager` class provides a convenient interface for common CRUD operations:

```python
from fantasy_premier_league.database.utils import DatabaseManager
from fantasy_premier_league.models import Player

player_manager = DatabaseManager(Player)

with get_db_session() as session:
    # Get by ID
    player = player_manager.get_by_id(session, 1)
    
    # Get all with limit
    players = player_manager.get_all(session, limit=10)
    
    # Filter by attributes
    midfielders = player_manager.filter_by(session, position="MID")
    
    # Count records
    total_players = player_manager.count(session)
    
    # Create new record
    new_player = player_manager.create(session, name="New Player", position="MID")
    
    # Update record
    updated_player = player_manager.update(session, 1, position="DEF")
    
    # Delete record
    deleted = player_manager.delete(session, 1)
```

## ORM Models

The models are located in `fantasy_premier_league/models/` and include:

- **Base**: Common base class with ID, timestamps, and utility methods
- **Player**: Individual football players
- **Team**: Premier League teams
- **Gameweek**: Individual gameweeks
- **PlayerGameweekHistory**: Player performance per gameweek
- **PlayerSeasonHistory**: Player performance per season

### Using Models

```python
from fantasy_premier_league.models import Player, Team

# Query with relationships
players = session.query(Player).join(Team).filter_by(position="MID").all()

for player in players:
    print(f"{player.name} plays for {player.team.name}")
    
    # Access related data
    for history in player.gameweek_history:
        print(f"  Gameweek {history.gameweek.number}: {history.points} points")
```

## Error Handling

The database modules include comprehensive error handling:

```python
try:
    with get_db_session() as session:
        # Your operations here
        pass
except Exception as e:
    print(f"Database error: {e}")
    # Session automatically rolls back on error
```

## Best Practices

1. **Always use context managers** for automatic transaction management
2. **Use ORM for simple operations** and raw SQL for complex queries
3. **Handle errors appropriately** - sessions automatically rollback on exceptions
4. **Use bulk operations** for large datasets
5. **Keep sessions short-lived** - don't hold them open for long periods

## Testing

To test the database connection:

```python
from fantasy_premier_league.database import get_db_session

with get_db_session() as session:
    result = session.execute("SELECT 1 as test").fetchone()
    if result and result[0] == 1:
        print("Database connection successful!")
    else:
        print("Database connection failed!")
```

## Examples

See `examples/database_usage.py` for comprehensive examples of all database operations.

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure all dependencies are installed (`psycopg2-binary`, `sqlalchemy`)
2. **Connection errors**: Check your `config.yaml` and database server status
3. **Session errors**: Ensure you're using context managers properly

### Debugging

Enable SQL query logging by setting `echo=True` in the engine configuration:

```python
# In config.py
def get_engine():
    database_url = get_database_url()
    return create_engine(
        database_url,
        future=True,
        echo=True,  # Enable SQL logging
        pool_pre_ping=True,
        pool_recycle=300
    )
``` 