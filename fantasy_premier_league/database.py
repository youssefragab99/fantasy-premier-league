"""
Legacy database module - now imports from the new modular structure.

This file maintains backward compatibility while the new modular
database structure is being adopted.
"""

# Import from the new modular database package
from .database import (
    DatabaseSession,
    get_database_url,
    get_db_session,
    get_engine,
    get_psycopg2_connection,
    get_session_factory,
)

# Re-export for backward compatibility
__all__ = [
    "DatabaseSession",
    "get_database_url",
    "get_db_session",
    "get_engine",
    "get_psycopg2_connection",
    "get_session_factory",
]
