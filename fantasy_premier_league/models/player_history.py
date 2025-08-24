"""
Player history models for Fantasy Premier League application.

This module defines models for tracking player performance
across gameweeks and seasons.
"""

from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Uuid,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class PlayerGameweekHistory(Base):
    """
    Player gameweek history model reflecting the player_gameweek_history table.

    Columns:
        player_id: uuid, not null
        gameweek: integer, not null
        season: varchar(10), not null
        fixture_id: integer, not null
        opponent_team_id: integer, not null
        total_points: integer, not null
        was_home: boolean, not null
        kickoff_time: timestamp (nullable)
        team_h_score: integer (nullable)
        team_a_score: integer (nullable)
        minutes: integer, not null
        goals_scored: integer, not null
        assists: integer, not null
        clean_sheets: integer, not null
        goals_conceded: integer, not null
        own_goals: integer, not null
        penalties_saved: integer, not null
        penalties_missed: integer, not null
        yellow_cards: integer, not null
        red_cards: integer, not null
        saves: integer, not null
        bonus: integer, not null
        bps: integer, not null
        influence: double precision (nullable)
        creativity: double precision (nullable)
        threat: double precision (nullable)
        ict_index: double precision (nullable)
        value: integer (nullable)
        selected: bigint (nullable)
        id: uuid, not null (inherited from Base)
    """

    __tablename__ = "player_gameweek_history"

    player_id: Mapped[Uuid] = mapped_column(Uuid, nullable=False)
    gameweek: Mapped[int] = mapped_column(Integer, nullable=False)
    season: Mapped[str] = mapped_column(String(10), nullable=False)
    fixture_id: Mapped[int] = mapped_column(Integer, nullable=False)
    opponent_team_id: Mapped[int] = mapped_column(Integer, nullable=False)
    total_points: Mapped[int] = mapped_column(Integer, nullable=False)
    was_home: Mapped[bool] = mapped_column(Boolean, nullable=False)
    kickoff_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    team_h_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_a_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    minutes: Mapped[int] = mapped_column(Integer, nullable=False)
    goals_scored: Mapped[int] = mapped_column(Integer, nullable=False)
    assists: Mapped[int] = mapped_column(Integer, nullable=False)
    clean_sheets: Mapped[int] = mapped_column(Integer, nullable=False)
    goals_conceded: Mapped[int] = mapped_column(Integer, nullable=False)
    own_goals: Mapped[int] = mapped_column(Integer, nullable=False)
    penalties_saved: Mapped[int] = mapped_column(Integer, nullable=False)
    penalties_missed: Mapped[int] = mapped_column(Integer, nullable=False)
    yellow_cards: Mapped[int] = mapped_column(Integer, nullable=False)
    red_cards: Mapped[int] = mapped_column(Integer, nullable=False)
    saves: Mapped[int] = mapped_column(Integer, nullable=False)
    bonus: Mapped[int] = mapped_column(Integer, nullable=False)
    bps: Mapped[int] = mapped_column(Integer, nullable=False)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    creativity: Mapped[float | None] = mapped_column(Float, nullable=True)
    threat: Mapped[float | None] = mapped_column(Float, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    value: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[BigInteger | None] = mapped_column(BigInteger, nullable=True)

    # Foreign key to all_players table for standardized name matching
    all_player_id: Mapped[Uuid | None] = mapped_column(
        Uuid, ForeignKey("all_players.id"), nullable=True, index=True
    )

    # Relationships
    all_player = relationship("AllPlayers")

    def __repr__(self) -> str:
        """String representation of the gameweek history."""
        return f"<PlayerGameweekHistory(player_id={self.player_id})>"


class PlayerSeasonHistory(Base):
    """
    Player performance summary for entire seasons.

    Attributes:
        player_id: ID of the player
        season_name: Season identifier (e.g., "2023-24")
        start_cost: Player cost at start of season
        end_cost: Player cost at end of season
        total_points: Total points for the season
        minutes: Total minutes played
        goals_scored: Total goals scored
        assists: Total assists provided
        clean_sheets: Total clean sheets
        goals_conceded: Total goals conceded
        own_goals: Total own goals
        penalties_saved: Total penalties saved
        penalties_missed: Total penalties missed
        yellow_cards: Total yellow cards
        red_cards: Total red cards
        saves: Total saves
        bonus: Total bonus points
        bps: Total bonus point system score
        influence: ICT influence score
        creativity: ICT creativity score
        threat: ICT threat score
        ict_index: ICT index score
        id: Unique identifier (UUID, inherited from Base)
    """

    __tablename__ = "player_season_history"

    # Foreign keys and identification
    player_id: Mapped[Uuid] = mapped_column(Uuid, nullable=False)
    season_name: Mapped[str] = mapped_column(String(10), nullable=False)  # e.g., "2023-24"

    # Season costs
    start_cost: Mapped[int | None] = mapped_column(Integer, nullable=True)
    end_cost: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # Season totals
    total_points: Mapped[int | None] = mapped_column(Integer, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    yellow_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    creativity: Mapped[float | None] = mapped_column(Float, nullable=True)
    threat: Mapped[float | None] = mapped_column(Float, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)

    # Foreign key to all_players table for standardized name matching
    all_player_id: Mapped[Uuid | None] = mapped_column(
        Uuid, ForeignKey("all_players.id"), nullable=True, index=True
    )

    # Relationships
    all_player = relationship("AllPlayers")

    def __repr__(self) -> str:
        """String representation of the season history."""
        return (
            f"<PlayerSeasonHistory("
            f"player_id={self.player_id}, "
            f"season_name='{self.season_name}')>"
        )
