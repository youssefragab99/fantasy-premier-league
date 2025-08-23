"""
Database utilities for Fantasy Premier League application.

This module provides common database operations, helper functions,
and utility classes for working with the database.
"""

from typing import Any, TypeVar

from sqlalchemy import text
from sqlalchemy.orm import Session

from ..models.base import Base
from .session import get_db_session

T = TypeVar("T", bound=Base)


class DatabaseManager:
    """
    Database manager providing common CRUD operations.

    This class provides a convenient interface for common database
    operations using SQLAlchemy ORM.
    """

    def __init__(self, model_class: type[T]):
        """
        Initialize the database manager.

        Args:
            model_class: The ORM model class to manage
        """
        self.model_class = model_class

    def get_by_id(self, session: Session, id: int) -> T | None:
        """
        Get a record by its ID.

        Args:
            session: Database session
            id: Record ID

        Returns:
            Model instance or None if not found
        """
        return session.query(self.model_class).filter_by(id=id).first()

    def get_all(self, session: Session, limit: int | None = None) -> list[T]:
        """
        Get all records.

        Args:
            session: Database session
            limit: Maximum number of records to return

        Returns:
            List of model instances
        """
        query = session.query(self.model_class)
        if limit:
            query = query.limit(limit)
        return query.all()

    def create(self, session: Session, **kwargs) -> T:
        """
        Create a new record.

        Args:
            session: Database session
            **kwargs: Model attributes

        Returns:
            Created model instance
        """
        instance = self.model_class(**kwargs)
        session.add(instance)
        session.flush()  # Get the ID without committing
        return instance

    def update(self, session: Session, id: int, **kwargs) -> T | None:
        """
        Update an existing record.

        Args:
            session: Database session
            id: Record ID
            **kwargs: Attributes to update

        Returns:
            Updated model instance or None if not found
        """
        instance = self.get_by_id(session, id)
        if instance:
            for key, value in kwargs.items():
                if hasattr(instance, key):
                    setattr(instance, key, value)
            session.flush()
        return instance

    def delete(self, session: Session, id: int) -> bool:
        """
        Delete a record.

        Args:
            session: Database session
            id: Record ID

        Returns:
            True if deleted, False if not found
        """
        instance = self.get_by_id(session, id)
        if instance:
            session.delete(instance)
            session.flush()
            return True
        return False

    def filter_by(self, session: Session, **kwargs) -> list[T]:
        """
        Filter records by attributes.

        Args:
            session: Database session
            **kwargs: Filter criteria

        Returns:
            List of matching model instances
        """
        return session.query(self.model_class).filter_by(**kwargs).all()

    def count(self, session: Session, **kwargs) -> int:
        """
        Count records matching criteria.

        Args:
            session: Database session
            **kwargs: Filter criteria

        Returns:
            Number of matching records
        """
        query = session.query(self.model_class)
        if kwargs:
            query = query.filter_by(**kwargs)
        return query.count()


def execute_raw_sql(query: str, params: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    """
    Execute raw SQL query and return results as dictionaries.

    Args:
        query: SQL query string
        params: Query parameters

    Returns:
        List of result dictionaries
    """
    with get_db_session() as session:
        result = session.execute(text(query), params or {})
        columns = result.keys()
        return [dict(zip(columns, row, strict=False)) for row in result.fetchall()]


def bulk_insert(model_class: type[T], data: list[dict[str, Any]]) -> list[T]:
    """
    Bulk insert multiple records.

    Args:
        model_class: The ORM model class
        data: List of dictionaries containing record data

    Returns:
        List of created model instances
    """
    with get_db_session() as session:
        instances = []
        for record_data in data:
            instance = model_class(**record_data)
            instances.append(instance)
            session.add(instance)

        session.flush()
        return instances


def bulk_update(model_class: type[T], updates: list[dict[str, Any]], id_field: str = "id") -> int:
    """
    Bulk update multiple records.

    Args:
        model_class: The ORM model class
        updates: List of dictionaries containing update data
        id_field: Field name to use for identifying records

    Returns:
        Number of updated records
    """
    with get_db_session() as session:
        updated_count = 0
        for update_data in updates:
            if id_field in update_data:
                record_id = update_data.pop(id_field)
                instance = session.query(model_class).filter_by(**{id_field: record_id}).first()
                if instance:
                    for key, value in update_data.items():
                        if hasattr(instance, key):
                            setattr(instance, key, value)
                    updated_count += 1

        session.flush()
        return updated_count
