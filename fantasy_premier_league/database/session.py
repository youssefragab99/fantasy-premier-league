"""
Database session management for Fantasy Premier League application.

This module provides session handling, context managers, and utility
functions for database operations using SQLAlchemy.

Usage:

    # Using the context manager function:
    from fantasy_premier_league.database.session import get_db_session

    with get_db_session() as session:
        players = session.query(Player).all()

    # Using the DatabaseSession class:
    from fantasy_premier_league.database.session import DatabaseSession

    with DatabaseSession() as session:
        teams = session.query(Team).all()

    # Or, for one-off queries:
    def get_player_count(session):
        return session.query(Player).count()

    db_session = DatabaseSession()
    count = db_session.execute_query(get_player_count)
"""

from collections.abc import Callable, Generator
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

    def __init__(self) -> None:
        self.session_factory = get_session_factory()
        self.session: Session | None = None

    def __enter__(self) -> Session | None:
        """Enter the session context."""
        self.session = self.session_factory()
        return self.session

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Exit the session context with proper cleanup."""
        if self.session is None:
            return

        try:
            if exc_type is None:
                self.session.commit()
            else:
                self.session.rollback()
        finally:
            self.session.close()
            self.session = None

    def execute_query(self, query_func: Callable[[Session], Any]) -> Any:
        """
        Execute a query function within a managed session context.

        Args:
            query_func: Function that takes a session and returns a result

        Returns:
            The result of the query function
        """
        with self as session:
            return query_func(session)
