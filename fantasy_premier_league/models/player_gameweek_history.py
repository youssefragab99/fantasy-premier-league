"""
Player gameweek history model for Fantasy Premier League application.

This module defines the PlayerGameweekHistory ORM model representing
the performance history of players in individual gameweeks.
"""

from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class PlayerGameweekHistory16_17(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2016_17"

    name: Mapped[str | None] = mapped_column(String, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    attempted_passes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    big_chances_created: Mapped[int | None] = mapped_column(Integer, nullable=True)
    big_chances_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clearances_blocks_interceptions: Mapped[int | None] = mapped_column(Integer, nullable=True)
    completed_passes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    # double precision in SQL, use String or Float
    creativity: Mapped[str | None] = mapped_column(String, nullable=True)
    dribbles: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ea_index: Mapped[int | None] = mapped_column(Integer, nullable=True)
    element: Mapped[int | None] = mapped_column(Integer, nullable=True)
    errors_leading_to_goal: Mapped[int | None] = mapped_column(Integer, nullable=True)
    errors_leading_to_goal_attempt: Mapped[int | None] = mapped_column(Integer, nullable=True)
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
    selected: Mapped[int | None] = mapped_column(Integer, nullable=True)
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


class PlayerGameweekHistory17_18(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2017_18"

    name = Column(String, nullable=True)
    assists = Column(Integer, nullable=True)
    attempted_passes = Column(Integer, nullable=True)
    big_chances_created = Column(Integer, nullable=True)
    big_chances_missed = Column(Integer, nullable=True)
    bonus = Column(Integer, nullable=True)
    bps = Column(Integer, nullable=True)
    clean_sheets = Column(Integer, nullable=True)
    clearances_blocks_interceptions = Column(Integer, nullable=True)
    completed_passes = Column(Integer, nullable=True)
    # double precision in SQL, use String or Float
    creativity = Column(String, nullable=True)
    dribbles = Column(Integer, nullable=True)
    ea_index = Column(Integer, nullable=True)
    element = Column(Integer, nullable=True)
    errors_leading_to_goal = Column(Integer, nullable=True)
    errors_leading_to_goal_attempt = Column(Integer, nullable=True)
    fixture = Column(Integer, nullable=True)
    fouls = Column(Integer, nullable=True)
    goals_conceded = Column(Integer, nullable=True)
    goals_scored = Column(Integer, nullable=True)
    # double precision in SQL, use String or Float
    ict_index = Column(String, nullable=True)
    # double precision in SQL, use String or Float
    influence = Column(String, nullable=True)
    key_passes = Column(Integer, nullable=True)
    kickoff_time = Column(String, nullable=True)
    kickoff_time_formatted = Column(String, nullable=True)
    loaned_in = Column(Integer, nullable=True)
    loaned_out = Column(Integer, nullable=True)
    minutes = Column(Integer, nullable=True)
    offside = Column(Integer, nullable=True)
    open_play_crosses = Column(Integer, nullable=True)
    opponent_team = Column(Integer, nullable=True)
    own_goals = Column(Integer, nullable=True)
    penalties_conceded = Column(Integer, nullable=True)
    penalties_missed = Column(Integer, nullable=True)
    penalties_saved = Column(Integer, nullable=True)
    recoveries = Column(Integer, nullable=True)
    red_cards = Column(Integer, nullable=True)
    round = Column(Integer, nullable=True)
    saves = Column(Integer, nullable=True)
    selected = Column(Integer, nullable=True)
    tackled = Column(Integer, nullable=True)
    tackles = Column(Integer, nullable=True)
    target_missed = Column(Integer, nullable=True)
    team_a_score = Column(Integer, nullable=True)
    team_h_score = Column(Integer, nullable=True)
    threat = Column(Integer, nullable=True)
    total_points = Column(Integer, nullable=True)
    transfers_balance = Column(Integer, nullable=True)
    transfers_in = Column(Integer, nullable=True)
    transfers_out = Column(Integer, nullable=True)
    value = Column(Integer, nullable=True)
    # boolean in SQL, use Boolean if imported
    was_home = Column(String, nullable=True)
    winning_goals = Column(Integer, nullable=True)
    yellow_cards = Column(Integer, nullable=True)
    GW = Column(Integer, nullable=True)


class PlayerGameweekHistory18_19(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2018_19"

    name: Mapped[str | None] = mapped_column(String, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    attempted_passes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    big_chances_created: Mapped[int | None] = mapped_column(Integer, nullable=True)
    big_chances_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bonus: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clean_sheets: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clearances_blocks_interceptions: Mapped[int | None] = mapped_column(Integer, nullable=True)
    completed_passes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    creativity: Mapped[float | None] = mapped_column(Float, nullable=True)
    dribbles: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ea_index: Mapped[int | None] = mapped_column(Integer, nullable=True)
    element: Mapped[int | None] = mapped_column(Integer, nullable=True)
    errors_leading_to_goal: Mapped[int | None] = mapped_column(Integer, nullable=True)
    errors_leading_to_goal_attempt: Mapped[int | None] = mapped_column(Integer, nullable=True)
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
    selected: Mapped[int | None] = mapped_column(Integer, nullable=True)
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


class PlayerGameweekHistory19_20(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2019_20"

    name = Column(String, nullable=True)
    assists = Column(Integer, nullable=True)
    bonus = Column(Integer, nullable=True)
    bps = Column(Integer, nullable=True)
    clean_sheets = Column(Integer, nullable=True)
    creativity = Column(Float, nullable=True)
    element = Column(Integer, nullable=True)
    fixture = Column(Integer, nullable=True)
    goals_conceded = Column(Integer, nullable=True)
    goals_scored = Column(Integer, nullable=True)
    ict_index = Column(Float, nullable=True)
    influence = Column(Float, nullable=True)
    kickoff_time = Column(String, nullable=True)
    minutes = Column(Integer, nullable=True)
    opponent_team = Column(Integer, nullable=True)
    own_goals = Column(Integer, nullable=True)
    penalties_missed = Column(Integer, nullable=True)
    penalties_saved = Column(Integer, nullable=True)
    red_cards = Column(Integer, nullable=True)
    round = Column(Integer, nullable=True)
    saves = Column(Integer, nullable=True)
    selected = Column(Integer, nullable=True)
    team_a_score = Column(Integer, nullable=True)
    team_h_score = Column(Integer, nullable=True)
    threat = Column(Float, nullable=True)
    total_points = Column(Integer, nullable=True)
    transfers_balance = Column(Integer, nullable=True)
    transfers_in = Column(Integer, nullable=True)
    transfers_out = Column(Integer, nullable=True)
    value = Column(Integer, nullable=True)
    was_home = Column(Boolean, nullable=True)
    winning_goals = Column(Integer, nullable=True)
    yellow_cards = Column(Integer, nullable=True)
    GW = Column(Integer, nullable=True)


class PlayerGameweekHistory20_21(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2020_21"

    name = Column(String, nullable=True)
    position = Column(String, nullable=True)
    team = Column(String, nullable=True)
    xP = Column(Float, nullable=True)
    assists = Column(Integer, nullable=True)
    bonus = Column(Integer, nullable=True)
    bps = Column(Integer, nullable=True)
    clean_sheets = Column(Integer, nullable=True)
    creativity = Column(Float, nullable=True)
    element = Column(Integer, nullable=True)
    fixture = Column(Integer, nullable=True)
    goals_conceded = Column(Integer, nullable=True)
    goals_scored = Column(Integer, nullable=True)
    ict_index = Column(Float, nullable=True)
    influence = Column(Float, nullable=True)
    kickoff_time = Column(String, nullable=True)
    minutes = Column(Integer, nullable=True)
    opponent_team = Column(Integer, nullable=True)
    own_goals = Column(Integer, nullable=True)
    penalties_missed = Column(Integer, nullable=True)
    penalties_saved = Column(Integer, nullable=True)
    red_cards = Column(Integer, nullable=True)
    round = Column(Integer, nullable=True)
    saves = Column(Integer, nullable=True)
    selected = Column(Integer, nullable=True)
    team_a_score = Column(Integer, nullable=True)
    team_h_score = Column(Integer, nullable=True)
    threat = Column(Float, nullable=True)
    total_points = Column(Integer, nullable=True)
    transfers_balance = Column(Integer, nullable=True)
    transfers_in = Column(Integer, nullable=True)
    transfers_out = Column(Integer, nullable=True)
    value = Column(Integer, nullable=True)
    was_home = Column(Boolean, nullable=True)
    yellow_cards = Column(Integer, nullable=True)
    GW = Column(Integer, nullable=True)


class PlayerGameweekHistory21_22(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2021_22"

    name = Column(String, nullable=True)
    position = Column(String, nullable=True)
    team = Column(String, nullable=True)
    xP = Column(Float, nullable=True)
    assists = Column(Integer, nullable=True)
    bonus = Column(Integer, nullable=True)
    bps = Column(Integer, nullable=True)
    clean_sheets = Column(Integer, nullable=True)
    creativity = Column(Float, nullable=True)
    element = Column(Integer, nullable=True)
    fixture = Column(Integer, nullable=True)
    goals_conceded = Column(Integer, nullable=True)
    goals_scored = Column(Integer, nullable=True)
    ict_index = Column(Float, nullable=True)
    influence = Column(Float, nullable=True)
    kickoff_time = Column(String, nullable=True)
    minutes = Column(Integer, nullable=True)
    opponent_team = Column(Integer, nullable=True)
    own_goals = Column(Integer, nullable=True)
    penalties_missed = Column(Integer, nullable=True)
    penalties_saved = Column(Integer, nullable=True)
    red_cards = Column(Integer, nullable=True)
    round = Column(Integer, nullable=True)
    saves = Column(Integer, nullable=True)
    selected = Column(Integer, nullable=True)
    team_a_score = Column(Integer, nullable=True)
    team_h_score = Column(Integer, nullable=True)
    threat = Column(Float, nullable=True)
    total_points = Column(Integer, nullable=True)
    transfers_balance = Column(Integer, nullable=True)
    transfers_in = Column(Integer, nullable=True)
    transfers_out = Column(Integer, nullable=True)
    value = Column(Integer, nullable=True)
    was_home = Column(Boolean, nullable=True)
    yellow_cards = Column(Integer, nullable=True)
    GW = Column(Integer, nullable=True)


class PlayerGameweekHistory22_23(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2022_23"

    name = Column(String, nullable=True)
    position = Column(String, nullable=True)
    team = Column(String, nullable=True)
    xP = Column(Float, nullable=True)
    assists = Column(Integer, nullable=True)
    bonus = Column(Integer, nullable=True)
    bps = Column(Integer, nullable=True)
    clean_sheets = Column(Integer, nullable=True)
    creativity = Column(Float, nullable=True)
    element = Column(Integer, nullable=True)
    expected_assists = Column(Float, nullable=True)
    expected_goal_involvements = Column(Float, nullable=True)
    expected_goals = Column(Float, nullable=True)
    expected_goals_conceded = Column(Float, nullable=True)
    fixture = Column(Integer, nullable=True)
    goals_conceded = Column(Integer, nullable=True)
    goals_scored = Column(Integer, nullable=True)
    ict_index = Column(Float, nullable=True)
    influence = Column(Float, nullable=True)
    kickoff_time = Column(String, nullable=True)
    minutes = Column(Integer, nullable=True)
    opponent_team = Column(Integer, nullable=True)
    own_goals = Column(Integer, nullable=True)
    penalties_missed = Column(Integer, nullable=True)
    penalties_saved = Column(Integer, nullable=True)
    red_cards = Column(Integer, nullable=True)
    round = Column(Integer, nullable=True)
    saves = Column(Integer, nullable=True)
    selected = Column(Integer, nullable=True)
    starts = Column(Integer, nullable=True)
    team_a_score = Column(Integer, nullable=True)
    team_h_score = Column(Integer, nullable=True)
    threat = Column(Float, nullable=True)
    total_points = Column(Integer, nullable=True)
    transfers_balance = Column(Integer, nullable=True)
    transfers_in = Column(Integer, nullable=True)
    transfers_out = Column(Integer, nullable=True)
    value = Column(Integer, nullable=True)
    was_home = Column(Boolean, nullable=True)
    yellow_cards = Column(Integer, nullable=True)
    GW = Column(Integer, nullable=True)


class PlayerGameweekHistory23_24(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2023_24"

    name = Column(String, nullable=True)
    position = Column(String, nullable=True)
    team = Column(String, nullable=True)
    xP = Column(Float, nullable=True)
    assists = Column(Integer, nullable=True)
    bonus = Column(Integer, nullable=True)
    bps = Column(Integer, nullable=True)
    clean_sheets = Column(Integer, nullable=True)
    creativity = Column(Float, nullable=True)
    element = Column(Integer, nullable=True)
    expected_assists = Column(Float, nullable=True)
    expected_goal_involvements = Column(Float, nullable=True)
    expected_goals = Column(Float, nullable=True)
    expected_goals_conceded = Column(Float, nullable=True)
    fixture = Column(Integer, nullable=True)
    goals_conceded = Column(Integer, nullable=True)
    goals_scored = Column(Integer, nullable=True)
    ict_index = Column(Float, nullable=True)
    influence = Column(Float, nullable=True)
    kickoff_time = Column(String, nullable=True)
    minutes = Column(Integer, nullable=True)
    opponent_team = Column(Integer, nullable=True)
    own_goals = Column(Integer, nullable=True)
    penalties_missed = Column(Integer, nullable=True)
    penalties_saved = Column(Integer, nullable=True)
    red_cards = Column(Integer, nullable=True)
    round = Column(Integer, nullable=True)
    saves = Column(Integer, nullable=True)
    selected = Column(Integer, nullable=True)
    starts = Column(Integer, nullable=True)
    team_a_score = Column(Integer, nullable=True)
    team_h_score = Column(Integer, nullable=True)
    threat = Column(Float, nullable=True)
    total_points = Column(Integer, nullable=True)
    transfers_balance = Column(Integer, nullable=True)
    transfers_in = Column(Integer, nullable=True)
    transfers_out = Column(Integer, nullable=True)
    value = Column(Integer, nullable=True)
    was_home = Column(Boolean, nullable=True)
    yellow_cards = Column(Integer, nullable=True)
    GW = Column(Integer, nullable=True)
