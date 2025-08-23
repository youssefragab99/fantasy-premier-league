"""
Team model for Fantasy Premier League application.

This module defines the Team ORM model representing football
teams in the Premier League.
"""

from sqlalchemy import Column, Integer, String

from .base import Base


class Team(Base):
    """
    Team model representing Premier League football teams.

    Attributes:
        name: Team name
        short_name: Abbreviated team name
        code: Team code used in FPL
    """

    id = Column(Integer, primary_key=True)

    # Team identification
    name = Column(String(100), nullable=False, unique=True, index=True)
    short_name = Column(String(20), nullable=False)
    code = Column(Integer, nullable=False, unique=True)

    def __repr__(self) -> str:
        """String representation of the team."""
        return f"<Team(name='{self.name}', code={self.code})>"
