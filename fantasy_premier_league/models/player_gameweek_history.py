"""
Player gameweek history model for Fantasy Premier League application.

This module defines the PlayerGameweekHistory ORM model representing
the performance history of players in individual gameweeks.
"""

from sqlalchemy import Boolean, Column, Float, Integer, String

from .base import Base


class PlayerGameweekHistory16_17(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2016_17"

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
    creativity = Column(String, nullable=True)  # double precision in SQL, use String or Float
    dribbles = Column(Integer, nullable=True)
    ea_index = Column(Integer, nullable=True)
    element = Column(Integer, nullable=True)
    errors_leading_to_goal = Column(Integer, nullable=True)
    errors_leading_to_goal_attempt = Column(Integer, nullable=True)
    fixture = Column(Integer, nullable=True)
    fouls = Column(Integer, nullable=True)
    goals_conceded = Column(Integer, nullable=True)
    goals_scored = Column(Integer, nullable=True)
    ict_index = Column(String, nullable=True)  # double precision in SQL, use String or Float
    id = Column(Integer, primary_key=True)
    influence = Column(String, nullable=True)  # double precision in SQL, use String or Float
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
    was_home = Column(String, nullable=True)  # boolean in SQL, use Boolean if imported
    winning_goals = Column(Integer, nullable=True)
    yellow_cards = Column(Integer, nullable=True)
    GW = Column(Integer, nullable=True)


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
    creativity = Column(String, nullable=True)  # double precision in SQL, use String or Float
    dribbles = Column(Integer, nullable=True)
    ea_index = Column(Integer, nullable=True)
    element = Column(Integer, nullable=True)
    errors_leading_to_goal = Column(Integer, nullable=True)
    errors_leading_to_goal_attempt = Column(Integer, nullable=True)
    fixture = Column(Integer, nullable=True)
    fouls = Column(Integer, nullable=True)
    goals_conceded = Column(Integer, nullable=True)
    goals_scored = Column(Integer, nullable=True)
    ict_index = Column(String, nullable=True)  # double precision in SQL, use String or Float
    id = Column(Integer, primary_key=True)
    influence = Column(String, nullable=True)  # double precision in SQL, use String or Float
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
    was_home = Column(String, nullable=True)  # boolean in SQL, use Boolean if imported
    winning_goals = Column(Integer, nullable=True)
    yellow_cards = Column(Integer, nullable=True)
    GW = Column(Integer, nullable=True)


class PlayerGameweekHistory18_19(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2018_19"

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
    creativity = Column(Float, nullable=True)
    dribbles = Column(Integer, nullable=True)
    ea_index = Column(Integer, nullable=True)
    element = Column(Integer, nullable=True)
    errors_leading_to_goal = Column(Integer, nullable=True)
    errors_leading_to_goal_attempt = Column(Integer, nullable=True)
    fixture = Column(Integer, nullable=True)
    fouls = Column(Integer, nullable=True)
    goals_conceded = Column(Integer, nullable=True)
    goals_scored = Column(Integer, nullable=True)
    ict_index = Column(Float, nullable=True)
    id = Column(Integer, primary_key=True)
    influence = Column(Float, nullable=True)
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


class PlayerGameweekHistory19_20(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2019_20"

    name = Column(String, nullable=True, primary_key=True)
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


class PlayerGameweekHistory20_21(Base):
    """
    Player gameweek history model representing individual gameweeks.
    """

    __tablename__ = "player_gameweek_history_2020_21"

    name = Column(String, nullable=True, primary_key=True)
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
