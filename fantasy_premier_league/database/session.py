"""
Database session management for Fantasy Premier League application.

This module provides session handling, context managers, and utility
functions for database operations using SQLAlchemy.
"""

from collections.abc import Generator
from contextlib import contextmanager
from typing import Any

from sqlalchemy.orm import Session

from .config import get_session_factory


@contextmanager
def get_db_session() -> Generator[Session, None, None]:
    """
    Context manager for database sessions.

    Yields:
        Session: SQLAlchemy database session

    Example:
        with get_db_session() as session:
            result = session.query(Player).all()
    """
    session_factory = get_session_factory()
    session = session_factory()

    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


class DatabaseSession:
    """
    Database session wrapper with automatic transaction management.

    This class provides a convenient way to manage database sessions
    with automatic commit/rollback on success/failure.
    """

    def __init__(self):
        self.session_factory = get_session_factory()
        self.session: Session | None = None

    def __enter__(self) -> Session:
        """Enter the session context."""
        self.session = self.session_factory()
        return self.session

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Exit the session context with proper cleanup."""
        if self.session is None:
            return

        try:
            if exc_type is None:
                # No exception occurred, commit the transaction
                self.session.commit()
            else:
                # Exception occurred, rollback the transaction
                self.session.rollback()
        finally:
            self.session.close()
            self.session = None

    def execute_query(self, query_func):
        """
        Execute a query function within a session context.

        Args:
            query_func: Function that takes a session and returns a result

        Returns:
            The result of the query function
        """
        with self as session:
            return query_func(session)
