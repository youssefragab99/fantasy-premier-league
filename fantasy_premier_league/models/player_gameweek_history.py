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

    name: Mapped[str | None] = mapped_column(String, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    attempted_passes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    big_chances_created: Mapped[int | None] = mapped_column(Integer, nullable=True)
    big_chances_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clearances_blocks_interceptions: Mapped[int | None] = mapped_column(
        Integer, nullable=True
    )
    completed_passes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    # double precision in SQL, use String or Float
    creativity: Mapped[str | None] = mapped_column(String, nullable=True)
    dribbles: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ea_index: Mapped[int | None] = mapped_column(Integer, nullable=True)
    element: Mapped[int | None] = mapped_column(Integer, nullable=True)
    errors_leading_to_goal: Mapped[int | None] = mapped_column(Integer, nullable=True)
    errors_leading_to_goal_attempt: Mapped[int | None] = mapped_column(
        Integer, nullable=True
    )
    fixture: Mapped[int | None] = mapped_column(Integer, nullable=True)
    fouls: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    # double precision in SQL, use String or Float
    ict_index: Mapped[str | None] = mapped_column(String, nullable=True)
    # double precision in SQL, use String or Float
    influence: Mapped[str | None] = mapped_column(String, nullable=True)
    key_passes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    kickoff_time: Mapped[str | None] = mapped_column(String, nullable=True)
    kickoff_time_formatted: Mapped[str | None] = mapped_column(String, nullable=True)
    loaned_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    loaned_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    offside: Mapped[int | None] = mapped_column(Integer, nullable=True)
    open_play_crosses: Mapped[int | None] = mapped_column(Integer, nullable=True)
    opponent_team: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    recoveries: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    round: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    tackled: Mapped[int | None] = mapped_column(Integer, nullable=True)
    tackles: Mapped[int | None] = mapped_column(Integer, nullable=True)
    target_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_a_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_h_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    threat: Mapped[int | None] = mapped_column(Integer, nullable=True)
    total_points: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_balance: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    value: Mapped[int | None] = mapped_column(Integer, nullable=True)
    # boolean in SQL, use Boolean if imported
    was_home: Mapped[str | None] = mapped_column(String, nullable=True)
    winning_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    yellow_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    GW: Mapped[int | None] = mapped_column(Integer, nullable=True)
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)


class PlayerGameweekHistory17_18(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2017_18"
    __table_args__ = {"extend_existing": True}

    name: Mapped[str | None] = mapped_column(String, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    attempted_passes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    big_chances_created: Mapped[int | None] = mapped_column(Integer, nullable=True)
    big_chances_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clearances_blocks_interceptions: Mapped[int | None] = mapped_column(
        Integer, nullable=True
    )
    completed_passes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    # double precision in SQL, use String or Float
    creativity: Mapped[str | None] = mapped_column(String, nullable=True)
    dribbles: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ea_index: Mapped[int | None] = mapped_column(Integer, nullable=True)
    element: Mapped[int | None] = mapped_column(Integer, nullable=True)
    errors_leading_to_goal: Mapped[int | None] = mapped_column(Integer, nullable=True)
    errors_leading_to_goal_attempt: Mapped[int | None] = mapped_column(
        Integer, nullable=True
    )
    fixture: Mapped[int | None] = mapped_column(Integer, nullable=True)
    fouls: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    key_passes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    kickoff_time: Mapped[str | None] = mapped_column(String, nullable=True)
    kickoff_time_formatted: Mapped[str | None] = mapped_column(String, nullable=True)
    loaned_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    loaned_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    offside: Mapped[int | None] = mapped_column(Integer, nullable=True)
    open_play_crosses: Mapped[int | None] = mapped_column(Integer, nullable=True)
    opponent_team: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    recoveries: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    round: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    tackled: Mapped[int | None] = mapped_column(Integer, nullable=True)
    tackles: Mapped[int | None] = mapped_column(Integer, nullable=True)
    target_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_a_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_h_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    threat: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_points: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_balance: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    value: Mapped[int | None] = mapped_column(Integer, nullable=True)
    was_home: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    winning_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    yellow_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    GW: Mapped[int | None] = mapped_column(Integer, nullable=True)
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)


class PlayerGameweekHistory18_19(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2018_19"
    __table_args__ = {"extend_existing": True}

    name: Mapped[str | None] = mapped_column(String, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    attempted_passes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    big_chances_created: Mapped[int | None] = mapped_column(Integer, nullable=True)
    big_chances_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clearances_blocks_interceptions: Mapped[int | None] = mapped_column(
        Integer, nullable=True
    )
    completed_passes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    creativity: Mapped[float | None] = mapped_column(Float, nullable=True)
    dribbles: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ea_index: Mapped[int | None] = mapped_column(Integer, nullable=True)
    element: Mapped[int | None] = mapped_column(Integer, nullable=True)
    errors_leading_to_goal: Mapped[int | None] = mapped_column(Integer, nullable=True)
    errors_leading_to_goal_attempt: Mapped[int | None] = mapped_column(
        Integer, nullable=True
    )
    fixture: Mapped[int | None] = mapped_column(Integer, nullable=True)
    fouls: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    key_passes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    kickoff_time: Mapped[str | None] = mapped_column(String, nullable=True)
    kickoff_time_formatted: Mapped[str | None] = mapped_column(String, nullable=True)
    loaned_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    loaned_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    offside: Mapped[int | None] = mapped_column(Integer, nullable=True)
    open_play_crosses: Mapped[int | None] = mapped_column(Integer, nullable=True)
    opponent_team: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    recoveries: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    round: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    tackled: Mapped[int | None] = mapped_column(Integer, nullable=True)
    tackles: Mapped[int | None] = mapped_column(Integer, nullable=True)
    target_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_a_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_h_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    threat: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_points: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_balance: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    value: Mapped[int | None] = mapped_column(Integer, nullable=True)
    was_home: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    winning_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    yellow_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    GW: Mapped[int | None] = mapped_column(Integer, nullable=True)
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)


class PlayerGameweekHistory19_20(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2019_20"
    __table_args__ = {"extend_existing": True}

    name: Mapped[str | None] = mapped_column(String, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    creativity: Mapped[float | None] = mapped_column(Float, nullable=True)
    element: Mapped[int | None] = mapped_column(Integer, nullable=True)
    fixture: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    kickoff_time: Mapped[str | None] = mapped_column(String, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    opponent_team: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    round: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    team_a_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_h_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    threat: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_points: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_balance: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    transfers_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    value: Mapped[int | None] = mapped_column(Integer, nullable=True)
    was_home: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    winning_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    yellow_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    GW: Mapped[int | None] = mapped_column(Integer, nullable=True)
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)


class PlayerGameweekHistory20_21(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2020_21"
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
    fixture: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    kickoff_time: Mapped[str | None] = mapped_column(String, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    opponent_team: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    round: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
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
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)


class PlayerGameweekHistory21_22(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2021_22"
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
    fixture: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ict_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    influence: Mapped[float | None] = mapped_column(Float, nullable=True)
    kickoff_time: Mapped[str | None] = mapped_column(String, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    opponent_team: Mapped[int | None] = mapped_column(Integer, nullable=True)
    own_goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalties_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red_cards: Mapped[int | None] = mapped_column(Integer, nullable=True)
    round: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)
    selected: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
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
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)


class PlayerGameweekHistory22_23(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2022_23"
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
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)


class PlayerGameweekHistory23_24(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2023_24"
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
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)


class PlayerGameweekHistory24_25(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2024_25"
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
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)
