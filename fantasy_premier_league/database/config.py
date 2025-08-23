"""
Database configuration module for Fantasy Premier League application.

This module handles database connection configuration, URL construction,
and engine creation for both SQLAlchemy and direct psycopg2 connections.
"""

import os
from pathlib import Path
from typing import Any

import yaml
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker


def load_config() -> dict[str, Any]:
    """Load database configuration from config.yaml file."""
    config_path = Path(__file__).parent.parent.parent / "config.yaml"

    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    try:
        with open(config_path, encoding="utf-8") as f:
            config = yaml.safe_load(f)

        if not config or "db" not in config:
            raise ValueError("Invalid configuration file: missing 'db' section")

        return config
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing configuration file: {e}") from e


def get_database_url() -> str:
    """
    Get database connection URL with fallback logic.

    Returns:
        str: Database connection URL

    Raises:
        ValueError: If configuration is invalid
    """
    # Check for environment variable first
    env_url = os.getenv("DATABASE_URL")
    if env_url:
        return env_url

    # Fallback to local docker-compose exposed Postgres
    try:
        config = load_config()
        db_config = config["db"]

        user = db_config.get("username")
        password = db_config.get("password")
        host = db_config.get("host")
        port = db_config.get("port")
        database = db_config.get("database")

        # Validate required fields
        if not all([user, password, host, port, database]):
            missing = [k for k, v in db_config.items() if not v]
            raise ValueError(f"Missing required database configuration: {missing}")

        # Use psycopg2 driver as per pyproject dependency
        return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

    except Exception as e:
        raise ValueError(f"Failed to construct database URL: {e}") from e


def get_engine() -> Engine:
    """
    Create and return SQLAlchemy engine.

    Returns:
        Engine: SQLAlchemy engine instance
    """
    database_url = get_database_url()
    return create_engine(
        database_url,
        future=True,
        pool_pre_ping=True,
        pool_recycle=300,
        echo=False,  # Set to True for SQL query logging
    )


def get_session_factory() -> sessionmaker:
    """
    Create and return SQLAlchemy session factory.

    Returns:
        sessionmaker: SQLAlchemy session factory
    """
    engine = get_engine()
    return sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
