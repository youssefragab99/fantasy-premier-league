"""
Player model for Fantasy Premier League application.

This module defines the Player ORM model representing individual
football players in the FPL system.
"""

from sqlalchemy import Boolean, Column, Float, Integer, String

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

    # Remove explicit __tablename__ to let Base generate it automatically
    id = Column(Integer, primary_key=True)

    # Player identification
    name = Column(String(100), nullable=False, index=True)
    team_id = Column(Integer, nullable=False)

    # Player attributes
    position = Column(String(3), nullable=False)  # GK, DEF, MID, FWD
    cost = Column(Float, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)

    def __repr__(self) -> str:
        """String representation of the player."""
        return f"<Player(name='{self.name}', position='{self.position}', team_id={self.team_id})>"
