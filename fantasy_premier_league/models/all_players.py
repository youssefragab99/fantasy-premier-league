"""
All players model for Fantasy Premier League application.

This module defines models for tracking all players in the Fantasy Premier League.
"""

from uuid import uuid4

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class AllPlayers(Base):
    """
    All players model for Fantasy Premier League application.

    This table serves as the master reference for all players across all seasons,
    using standardized names for consistent matching.
    """

    __tablename__ = "all_players"

    id: Mapped[Uuid] = mapped_column(Uuid, primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)

    # Relationships
    players = relationship("Player", back_populates="all_player")

    def __repr__(self) -> str:
        """String representation of the all player."""
        return f"<AllPlayers(id={self.id}, name='{self.name}')>"
