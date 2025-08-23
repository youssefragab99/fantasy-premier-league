"""
Direct psycopg2 connection management for Fantasy Premier League application.

This module provides direct database connections using psycopg2 for
raw SQL operations and bulk data operations.
"""

from contextlib import contextmanager
from typing import Any

import psycopg2

from .config import load_config


def get_psycopg2_connection_params() -> dict[str, str]:
    """
    Get psycopg2 connection parameters from configuration.

    Returns:
        Dict containing connection parameters

    Raises:
        ValueError: If configuration is invalid
    """
    try:
        config = load_config()
        db_config = config["db"]

        return {
            "host": db_config["host"],
            "port": db_config["port"],
            "database": db_config["database"],
            "user": db_config["username"],
            "password": db_config["password"],
        }
    except Exception as e:
        raise ValueError(f"Failed to load connection parameters: {e}")


@contextmanager
def get_psycopg2_connection():
    """
    Context manager for psycopg2 connections.

    Yields:
        psycopg2.extensions.connection: Database connection

    Example:
        with get_psycopg2_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM players")
                results = cur.fetchall()
    """
    params = get_psycopg2_connection_params()
    conn = None

    try:
        conn = psycopg2.connect(**params)
        yield conn
    except Exception:
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()


def execute_query(query: str, params: tuple | None = None) -> list[tuple]:
    """
    Execute a SELECT query and return results.

    Args:
        query: SQL query string
        params: Query parameters (optional)

    Returns:
        List of result tuples
    """
    with get_psycopg2_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            return cur.fetchall()


def execute_command(command: str, params: tuple | None = None) -> int:
    """
    Execute a non-SELECT command (INSERT, UPDATE, DELETE).

    Args:
        command: SQL command string
        params: Command parameters (optional)

    Returns:
        Number of affected rows
    """
    with get_psycopg2_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(command, params)
            conn.commit()
            return cur.rowcount


def execute_many(command: str, params_list: list[tuple]) -> int:
    """
    Execute a command with multiple parameter sets.

    Args:
        command: SQL command string
        params_list: List of parameter tuples

    Returns:
        Number of affected rows
    """
    with get_psycopg2_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(command, params_list)
            conn.commit()
            return cur.rowcount


def get_table_names() -> list[str]:
    """
    Get list of all table names in the database.

    Returns:
        List of table names
    """
    query = """
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
        ORDER BY table_name
    """
    results = execute_query(query)
    return [row[0] for row in results]


def get_table_info(table_name: str) -> dict[str, Any]:
    """
    Get information about a specific table.

    Args:
        table_name: Name of the table

    Returns:
        Dictionary containing table information
    """
    query = """
        SELECT column_name, data_type, is_nullable, column_default
        FROM information_schema.columns
        WHERE table_name = %s
        ORDER BY ordinal_position
    """
    results = execute_query(query, (table_name,))

    columns = []
    for row in results:
        columns.append(
            {"name": row[0], "type": row[1], "nullable": row[2] == "YES", "default": row[3]}
        )

    return {"table_name": table_name, "columns": columns, "column_count": len(columns)}
