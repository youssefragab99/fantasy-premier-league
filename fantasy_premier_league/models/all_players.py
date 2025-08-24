"""
All players model for Fantasy Premier League application.

This module defines models for tracking all players in the Fantasy Premier League.
"""

from uuid import uuid4

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class AllPlayers(Base):
    """
    All players model for Fantasy Premier League application.
    """

    __tablename__ = "all_players"

    id: Mapped[Uuid] = mapped_column(Uuid, primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
