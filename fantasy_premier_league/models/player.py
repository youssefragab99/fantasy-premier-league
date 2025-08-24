"""
Player model for Fantasy Premier League application.

This module defines the Player ORM model representing individual
football players in the FPL system.
"""

from sqlalchemy import ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Player(Base):
    """
    Player model representing individual football players.

    Attributes:
        first_name: Player's first name
        second_name: Player's last name
        web_name: Player's display name for web
        team_id: ID of the team the player belongs to
        element_type: Player's position type (1=GK, 2=DEF, 3=MID, 4=FWD)
        fpl_id: Original FPL API ID
        all_player_id: Foreign key to all_players table for standardized name matching
    """

    __tablename__ = "players"

    # Player identification
    fpl_id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True, index=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    second_name: Mapped[str] = mapped_column(String(100), nullable=False)
    web_name: Mapped[str] = mapped_column(String(100), nullable=True, index=True)
    now_cost: Mapped[int] = mapped_column(Integer, nullable=True)
    team_id: Mapped[int] = mapped_column(Integer, nullable=False)

    # Player attributes
    element_type: Mapped[int] = mapped_column(Integer, nullable=False)  # 1=GK, 2=DEF, 3=MID, 4=FWD

    # Foreign key to all_players table for standardized name matching
    all_player_id: Mapped[Uuid | None] = mapped_column(
        Uuid, ForeignKey("all_players.id"), nullable=True, index=True
    )

    # Relationship to all_players table
    all_player = relationship("AllPlayers", back_populates="players")

    def __repr__(self) -> str:
        """String representation of the player."""
        return (
            f"<Player("
            f"name='{self.first_name} {self.second_name}', "
            f"web_name='{self.web_name}', "
            f"team_id={self.team_id})>"
        )
