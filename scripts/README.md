# Database Reset Scripts

This directory contains scripts for managing the Fantasy Premier League database.

## Scripts

### `drop_and_restart.py`

A Python script that drops all existing database tables and recreates the schema from scratch.

**Features:**
- Safely drops all tables with CASCADE to handle dependencies
- Recreates the complete database schema
- Provides detailed feedback on the process
- Handles PostgreSQL-specific syntax

**Usage:**
```bash
# Run from project root directory
python scripts/drop_and_restart.py
```

### `run_drop_and_restart.sh`

A shell script wrapper that provides additional safety checks and a user-friendly interface.

**Features:**
- Verifies you're in the correct directory
- Provides clear error messages
- Runs the Python script with proper error handling

**Usage:**
```bash
# Run from project root directory
./scripts/run_drop_and_restart.sh
```

## When to Use

Use these scripts when you want to:
- Start fresh with a clean database
- Reset after major schema changes
- Troubleshoot database corruption issues
- Prepare for a new data loading session

## ⚠️ Warning

**These scripts will permanently delete all data in your database!** Make sure you have:
- Backed up any important data
- Confirmed you want to start fresh
- Stopped any running applications that use the database

## Prerequisites

- Python 3.8+
- SQLAlchemy
- PostgreSQL database connection
- Proper database configuration in `config.yaml` or environment variables

## After Running

Once the reset is complete:
1. Run your data loading scripts to populate the database
2. Verify data integrity with your validation scripts
3. Test your application with the fresh database

## Troubleshooting

If you encounter errors:
1. Check your database connection settings
2. Ensure you have proper permissions on the database
3. Verify all required Python packages are installed
4. Check the database logs for additional error details 