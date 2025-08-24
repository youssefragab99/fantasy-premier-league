"""
Base model class for Fantasy Premier League ORM models.

This module provides the base class that all database models inherit from,
including common fields and utility methods.
"""

import uuid
from datetime import datetime
from typing import Any

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    Base class for all ORM models.

    Provides common fields and methods that all models inherit.
    """

    @declared_attr
    def id(cls) -> Mapped[uuid.UUID]:
        """UUID primary key for all models."""
        return mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    def to_dict(self) -> dict[str, Any]:
        """
        Convert model instance to dictionary.

        Returns:
            Dictionary representation of the model
        """
        result = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            if isinstance(value, datetime):
                result[column.name] = value.isoformat()
            elif isinstance(value, uuid.UUID):
                result[column.name] = str(value)
            else:
                result[column.name] = value
        return result

    def __repr__(self) -> str:
        """String representation of the model."""
        return f"<{self.__class__.__name__}(id={self.id})>"
