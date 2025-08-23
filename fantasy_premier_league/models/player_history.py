"""
Player history models for Fantasy Premier League application.

This module defines models for tracking player performance
across gameweeks and seasons.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class PlayerGameweekHistory(Base):
    """
    Player performance history for individual gameweeks.

    Attributes:
        player_id: ID of the player
        gameweek_id: ID of the gameweek
        points: Points scored in the gameweek
        goals: Goals scored
        assists: Assists provided
        clean_sheets: Clean sheets kept
        bonus: Bonus points earned
    """

    __tablename__ = "player_gameweek_history"

    # Foreign keys
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    gameweek_id = Column(Integer, ForeignKey("gameweeks.id"), nullable=False)

    # Performance metrics
    points = Column(Integer, nullable=True)
    goals = Column(Integer, default=0, nullable=False)
    assists = Column(Integer, default=0, nullable=False)
    clean_sheets = Column(Integer, default=0, nullable=False)
    bonus = Column(Integer, default=0, nullable=False)

    # Relationships
    player = relationship("Player", back_populates="gameweek_history")
    gameweek = relationship("Gameweek", back_populates="player_history")

    def __repr__(self) -> str:
        """String representation of the gameweek history."""
        return (
            f"<PlayerGameweekHistory(player_id={self.player_id}, gameweek_id={self.gameweek_id})>"
        )


class PlayerSeasonHistory(Base):
    """
    Player performance summary for entire seasons.

    Attributes:
        player_id: ID of the player
        season: Season identifier
        total_points: Total points for the season
        total_goals: Total goals scored
        total_assists: Total assists provided
        appearances: Number of appearances
    """

    __tablename__ = "player_season_history"

    # Foreign keys and identification
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    season = Column(String(9), nullable=False)  # e.g., "2023-24"

    # Season totals
    total_points = Column(Integer, default=0, nullable=False)
    total_goals = Column(Integer, default=0, nullable=False)
    total_assists = Column(Integer, default=0, nullable=False)
    appearances = Column(Integer, default=0, nullable=False)

    # Relationships
    player = relationship("Player", back_populates="season_history")

    def __repr__(self) -> str:
        """String representation of the season history."""
        return f"<PlayerSeasonHistory(player_id={self.player_id}, season='{self.season}')>"
