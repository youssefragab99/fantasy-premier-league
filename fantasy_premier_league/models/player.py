"""
Player model for Fantasy Premier League application.

This module defines the Player ORM model representing individual
football players in the FPL system.
"""

from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Player(Base):
    """
    Player model representing individual football players.

    Attributes:
        name: Player's full name
        team_id: ID of the team the player belongs to
        position: Player's position (GK, DEF, MID, FWD)
        cost: Player's cost in FPL
        is_active: Whether the player is currently active
    """

    __tablename__ = "players"

    # Player identification
    name = Column(String(100), nullable=False, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)

    # Player attributes
    position = Column(String(3), nullable=False)  # GK, DEF, MID, FWD
    cost = Column(Float, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)

    # Relationships
    team = relationship("Team", back_populates="players")
    gameweek_history = relationship("PlayerGameweekHistory", back_populates="player")
    season_history = relationship("PlayerSeasonHistory", back_populates="player")

    def __repr__(self) -> str:
        """String representation of the player."""
        return f"<Player(name='{self.name}', position='{self.position}', team_id={self.team_id})>"
