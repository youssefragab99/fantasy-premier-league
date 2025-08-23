"""
Gameweek model for Fantasy Premier League application.

This module defines the Gameweek ORM model representing
individual gameweeks in the FPL season.
"""

from sqlalchemy import Boolean, Column, Date, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Gameweek(Base):
    """
    Gameweek model representing individual gameweeks.

    Attributes:
        number: Gameweek number
        season: Season identifier
        start_date: Start date of the gameweek
        is_finished: Whether the gameweek is completed
    """

    __tablename__ = "gameweeks"

    # Gameweek identification
    number = Column(Integer, nullable=False)
    season = Column(String(9), nullable=False)  # e.g., "2023-24"
    start_date = Column(Date, nullable=True)
    is_finished = Column(Boolean, default=False, nullable=False)

    # Relationships
    player_history = relationship("PlayerGameweekHistory", back_populates="gameweek")

    def __repr__(self) -> str:
        """String representation of the gameweek."""
        return f"<Gameweek(number={self.number}, season='{self.season}')>"
