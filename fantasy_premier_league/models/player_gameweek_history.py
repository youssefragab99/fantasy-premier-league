"""
Player gameweek history model for Fantasy Premier League application.

This module defines the PlayerGameweekHistory ORM model representing
the performance history of players in individual gameweeks.
"""

from uuid import uuid4

from sqlalchemy import UUID, BigInteger, Boolean, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class PlayerGameweekHistory16_17(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2016_17"
    __table_args__ = {"extend_existing": True}

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)
    name: Mapped[str | None] = mapped_column(String, nullable=True)
    position: Mapped[str | None] = mapped_column(String, nullable=True)
    team: Mapped[str | None] = mapped_column(String, nullable=True)
    xP: Mapped[float | None] = mapped_column(Float, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    creativity: Mapped[float | None] = mapped_column(Float, nullable=True)
    element: Mapped[int | None] = mapped_column(Integer, nullable=True)
    expected_assists: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goal_involvements: Mapped[float | None] = mapped_column(
        Float, nullable=True
    )
    expected_goals: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goals_conceded: Mapped[float | None] = mapped_column(Float, nullable=True)
    fixture: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    kickoff_time: Mapped[str | None] = mapped_column(String, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    modified: Mapped[str | None] = mapped_column(String, nullable=True)
    opponent_team: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    round: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    starts: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_a_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_h_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    threat: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_points: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_balance: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    value: Mapped[int | None] = mapped_column(Integer, nullable=True)
    was_home: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    yellow_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    GW: Mapped[int | None] = mapped_column(Integer, nullable=True)
    all_player_id: Mapped[UUID | None] = mapped_column(UUID, nullable=True)


class PlayerGameweekHistory17_18(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2017_18"
    __table_args__ = {"extend_existing": True}

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)
    name: Mapped[str | None] = mapped_column(String, nullable=True)
    position: Mapped[str | None] = mapped_column(String, nullable=True)
    team: Mapped[str | None] = mapped_column(String, nullable=True)
    xP: Mapped[float | None] = mapped_column(Float, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    creativity: Mapped[float | None] = mapped_column(Float, nullable=True)
    element: Mapped[int | None] = mapped_column(Integer, nullable=True)
    expected_assists: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goal_involvements: Mapped[float | None] = mapped_column(
        Float, nullable=True
    )
    expected_goals: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goals_conceded: Mapped[float | None] = mapped_column(Float, nullable=True)
    fixture: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    kickoff_time: Mapped[str | None] = mapped_column(String, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    modified: Mapped[str | None] = mapped_column(String, nullable=True)
    opponent_team: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    round: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    starts: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_a_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_h_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    threat: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_points: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_balance: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    value: Mapped[int | None] = mapped_column(Integer, nullable=True)
    was_home: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    yellow_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    GW: Mapped[int | None] = mapped_column(Integer, nullable=True)
    all_player_id: Mapped[UUID | None] = mapped_column(UUID, nullable=True)


class PlayerGameweekHistory18_19(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2018_19"
    __table_args__ = {"extend_existing": True}

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)
    name: Mapped[str | None] = mapped_column(String, nullable=True)
    position: Mapped[str | None] = mapped_column(String, nullable=True)
    team: Mapped[str | None] = mapped_column(String, nullable=True)
    xP: Mapped[float | None] = mapped_column(Float, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    creativity: Mapped[float | None] = mapped_column(Float, nullable=True)
    element: Mapped[int | None] = mapped_column(Integer, nullable=True)
    expected_assists: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goal_involvements: Mapped[float | None] = mapped_column(
        Float, nullable=True
    )
    expected_goals: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goals_conceded: Mapped[float | None] = mapped_column(Float, nullable=True)
    fixture: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    kickoff_time: Mapped[str | None] = mapped_column(String, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    modified: Mapped[str | None] = mapped_column(String, nullable=True)
    opponent_team: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    round: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    starts: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_a_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_h_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    threat: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_points: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_balance: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    value: Mapped[int | None] = mapped_column(Integer, nullable=True)
    was_home: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    yellow_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    GW: Mapped[int | None] = mapped_column(Integer, nullable=True)
    all_player_id: Mapped[UUID | None] = mapped_column(UUID, nullable=True)


class PlayerGameweekHistory19_20(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2019_20"
    __table_args__ = {"extend_existing": True}

    name: Mapped[str | None] = mapped_column(String, nullable=True)
    position: Mapped[str | None] = mapped_column(String, nullable=True)
    team: Mapped[str | None] = mapped_column(String, nullable=True)
    xP: Mapped[float | None] = mapped_column(Float, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    creativity: Mapped[float | None] = mapped_column(Float, nullable=True)
    element: Mapped[int | None] = mapped_column(Integer, nullable=True)
    expected_assists: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goal_involvements: Mapped[float | None] = mapped_column(
        Float, nullable=True
    )
    expected_goals: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goals_conceded: Mapped[float | None] = mapped_column(Float, nullable=True)
    fixture: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    kickoff_time: Mapped[str | None] = mapped_column(String, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    modified: Mapped[str | None] = mapped_column(String, nullable=True)
    opponent_team: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    round: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    starts: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_a_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_h_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    threat: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_points: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_balance: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    value: Mapped[int | None] = mapped_column(Integer, nullable=True)
    was_home: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    yellow_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    GW: Mapped[int | None] = mapped_column(Integer, nullable=True)
    all_player_id: Mapped[UUID | None] = mapped_column(UUID, nullable=True)
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)


class PlayerGameweekHistory20_21(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2020_21"
    __table_args__ = {"extend_existing": True}

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)
    name: Mapped[str | None] = mapped_column(String, nullable=True)
    position: Mapped[str | None] = mapped_column(String, nullable=True)
    team: Mapped[str | None] = mapped_column(String, nullable=True)
    xP: Mapped[float | None] = mapped_column(Float, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    creativity: Mapped[float | None] = mapped_column(Float, nullable=True)
    element: Mapped[int | None] = mapped_column(Integer, nullable=True)
    expected_assists: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goal_involvements: Mapped[float | None] = mapped_column(
        Float, nullable=True
    )
    expected_goals: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goals_conceded: Mapped[float | None] = mapped_column(Float, nullable=True)
    fixture: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    kickoff_time: Mapped[str | None] = mapped_column(String, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    modified: Mapped[str | None] = mapped_column(String, nullable=True)
    opponent_team: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    round: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    starts: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_a_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_h_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    threat: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_points: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_balance: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    value: Mapped[int | None] = mapped_column(Integer, nullable=True)
    was_home: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    yellow_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    GW: Mapped[int | None] = mapped_column(Integer, nullable=True)
    all_player_id: Mapped[UUID | None] = mapped_column(UUID, nullable=True)


class PlayerGameweekHistory21_22(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2021_22"
    __table_args__ = {"extend_existing": True}

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)
    name: Mapped[str | None] = mapped_column(String, nullable=True)
    position: Mapped[str | None] = mapped_column(String, nullable=True)
    team: Mapped[str | None] = mapped_column(String, nullable=True)
    xP: Mapped[float | None] = mapped_column(Float, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    creativity: Mapped[float | None] = mapped_column(Float, nullable=True)
    element: Mapped[int | None] = mapped_column(Integer, nullable=True)
    expected_assists: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goal_involvements: Mapped[float | None] = mapped_column(
        Float, nullable=True
    )
    expected_goals: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goals_conceded: Mapped[float | None] = mapped_column(Float, nullable=True)
    fixture: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    kickoff_time: Mapped[str | None] = mapped_column(String, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    modified: Mapped[str | None] = mapped_column(String, nullable=True)
    opponent_team: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    round: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    starts: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_a_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_h_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    threat: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_points: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_balance: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    value: Mapped[int | None] = mapped_column(Integer, nullable=True)
    was_home: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    yellow_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    GW: Mapped[int | None] = mapped_column(Integer, nullable=True)
    all_player_id: Mapped[UUID | None] = mapped_column(UUID, nullable=True)


class PlayerGameweekHistory22_23(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2022_23"
    __table_args__ = {"extend_existing": True}

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)
    name: Mapped[str | None] = mapped_column(String, nullable=True)
    position: Mapped[str | None] = mapped_column(String, nullable=True)
    team: Mapped[str | None] = mapped_column(String, nullable=True)
    xP: Mapped[float | None] = mapped_column(Float, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    creativity: Mapped[float | None] = mapped_column(Float, nullable=True)
    element: Mapped[int | None] = mapped_column(Integer, nullable=True)
    expected_assists: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goal_involvements: Mapped[float | None] = mapped_column(
        Float, nullable=True
    )
    expected_goals: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goals_conceded: Mapped[float | None] = mapped_column(Float, nullable=True)
    fixture: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    kickoff_time: Mapped[str | None] = mapped_column(String, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    modified: Mapped[str | None] = mapped_column(String, nullable=True)
    opponent_team: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    round: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    starts: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_a_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_h_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    threat: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_points: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_balance: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    value: Mapped[int | None] = mapped_column(Integer, nullable=True)
    was_home: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    yellow_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    GW: Mapped[int | None] = mapped_column(Integer, nullable=True)
    all_player_id: Mapped[UUID | None] = mapped_column(UUID, nullable=True)


class PlayerGameweekHistory23_24(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2023_24"
    __table_args__ = {"extend_existing": True}

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)
    name: Mapped[str | None] = mapped_column(String, nullable=True)
    position: Mapped[str | None] = mapped_column(String, nullable=True)
    team: Mapped[str | None] = mapped_column(String, nullable=True)
    xP: Mapped[float | None] = mapped_column(Float, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    creativity: Mapped[float | None] = mapped_column(Float, nullable=True)
    element: Mapped[int | None] = mapped_column(Integer, nullable=True)
    expected_assists: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goal_involvements: Mapped[float | None] = mapped_column(
        Float, nullable=True
    )
    expected_goals: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goals_conceded: Mapped[float | None] = mapped_column(Float, nullable=True)
    fixture: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    kickoff_time: Mapped[str | None] = mapped_column(String, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    modified: Mapped[str | None] = mapped_column(String, nullable=True)
    opponent_team: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    round: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    starts: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_a_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_h_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    threat: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_points: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_balance: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    value: Mapped[int | None] = mapped_column(Integer, nullable=True)
    was_home: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    yellow_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    GW: Mapped[int | None] = mapped_column(Integer, nullable=True)
    all_player_id: Mapped[UUID | None] = mapped_column(UUID, nullable=True)


class PlayerGameweekHistory24_25(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2024_25"
    __table_args__ = {"extend_existing": True}

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)
    name: Mapped[str | None] = mapped_column(String, nullable=True)
    position: Mapped[str | None] = mapped_column(String, nullable=True)
    team: Mapped[str | None] = mapped_column(String, nullable=True)
    xP: Mapped[float | None] = mapped_column(Float, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    creativity: Mapped[float | None] = mapped_column(Float, nullable=True)
    element: Mapped[int | None] = mapped_column(Integer, nullable=True)
    expected_assists: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goal_involvements: Mapped[float | None] = mapped_column(
        Float, nullable=True
    )
    expected_goals: Mapped[float | None] = mapped_column(Float, nullable=True)
    expected_goals_conceded: Mapped[float | None] = mapped_column(Float, nullable=True)
    fixture: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    kickoff_time: Mapped[str | None] = mapped_column(String, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    modified: Mapped[str | None] = mapped_column(String, nullable=True)
    opponent_team: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    round: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    starts: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_a_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_h_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    threat: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_points: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_balance: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    value: Mapped[int | None] = mapped_column(Integer, nullable=True)
    was_home: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    yellow_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    GW: Mapped[int | None] = mapped_column(Integer, nullable=True)
    all_player_id: Mapped[UUID | None] = mapped_column(UUID, nullable=True)
