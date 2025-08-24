"""
Team model for Fantasy Premier League application.

This module defines the Team ORM model representing football
teams in the Premier League.
"""

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Team(Base):
    """
    Team model representing Premier League football teams.

    Attributes:
        name: Team name
        short_name: Abbreviated team name
        code: Team code used in FPL
        fpl_id: Original FPL API ID
    """

    __tablename__ = "teams"

    # Team identification
    fpl_id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    short_name: Mapped[str] = mapped_column(String(20), nullable=False)
    code: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    strength_attack_home: Mapped[int] = mapped_column(Integer, nullable=True)
    strength_attack_away: Mapped[int] = mapped_column(Integer, nullable=True)
    strength_defence_home: Mapped[int] = mapped_column(Integer, nullable=True)
    strength_defence_away: Mapped[int] = mapped_column(Integer, nullable=True)
    strength_overall_home: Mapped[int] = mapped_column(Integer, nullable=True)
    strength_overall_away: Mapped[int] = mapped_column(Integer, nullable=True)

    def __repr__(self) -> str:
        """String representation of the team."""
        return f"<Team(name='{self.name}', code={self.code})>"
