#!/usr/bin/env python3
"""
Script to populate foreign key relationships to the all_players table.

This script matches players across all tables using standardized names
from the all_players table as the base for consistent player identification.
"""

import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import after path setup - noqa: E402
from fantasy_premier_league.data_utils.data_loading import convert_name  # noqa: E402
from fantasy_premier_league.database.connection import execute_command, execute_query  # noqa: E402


def get_all_players_mapping():
    """Get mapping of standardized names to all_players IDs."""
    query = "SELECT id, name FROM all_players"
    results = execute_query(query)

    # Create mapping: standardized_name -> all_player_id
    mapping = {}
    for row in results:
        all_player_id, standardized_name = row
        mapping[standardized_name] = all_player_id

    print(f"Found {len(mapping)} players in all_players table")
    return mapping


def update_players_table(all_players_mapping):
    """Update players table with all_player_id foreign keys."""
    print("\nUpdating players table...")

    # Get all players from the players table
    query = "SELECT id, first_name, second_name, web_name FROM players"
    results = execute_query(query)

    updated_count = 0
    not_found_count = 0

    for row in results:
        player_id, first_name, second_name, web_name = row

        # Try different name combinations for matching
        name_combinations = [
            f"{first_name} {second_name}".strip(),
            web_name if web_name else "",
            first_name,
            second_name,
        ]

        # Find matching standardized name
        matched_all_player_id = None
        for name_combo in name_combinations:
            if name_combo:
                standardized_name = convert_name(name_combo)
                if standardized_name in all_players_mapping:
                    matched_all_player_id = all_players_mapping[standardized_name]
                    break

        if matched_all_player_id:
            # Update the player record
            update_query = """
                UPDATE players 
                SET all_player_id = %s 
                WHERE id = %s
            """
            execute_command(update_query, (matched_all_player_id, player_id))
            updated_count += 1
        else:
            not_found_count += 1
            print(f"  - No match found for: {first_name} {second_name} ({web_name})")

    print(f"  - Updated: {updated_count}")
    print(f"  - Not found: {not_found_count}")
    return updated_count, not_found_count


# def update_player_season_history(all_players_mapping):
#     """Update player_season_history table with all_player_id foreign keys."""
#     print("\nUpdating player_season_history table...")

#     # Get all unique player names from the season history table
#     query = "SELECT DISTINCT name FROM player_season_history WHERE name IS NOT NULL"
#     results = execute_query(query)

#     updated_count = 0
#     not_found_count = 0

#     for row in results:
#         player_name = row[0]
#         if player_name:
#             standardized_name = convert_name(player_name)

#             if standardized_name in all_players_mapping:
#                 all_player_id = all_players_mapping[standardized_name]

#                 # Update all records with this player name
#                 update_query = """
#                     UPDATE player_season_history
#                     SET all_player_id = %s
#                     WHERE name = %s
#                 """
#                 affected_rows = execute_command(update_query, (all_player_id, player_name))
#                 updated_count += affected_rows
#             else:
#                 not_found_count += 1
#                 print(f"  - No match found for: {player_name}")

#     print(f"  - Updated records: {updated_count}")
#     print(f"  - Names not found: {not_found_count}")
#     return updated_count, not_found_count


def update_historical_season_tables(all_players_mapping) -> tuple[int, int]:
    """Update historical season tables with all_player_id foreign keys."""
    print("\nUpdating historical season tables...")

    # List of historical season tables
    historical_tables = [
        "player_gameweek_history_2016_17",
        "player_gameweek_history_2017_18",
        "player_gameweek_history_2018_19",
        "player_gameweek_history_2019_20",
        "player_gameweek_history_2020_21",
        "player_gameweek_history_2021_22",
        "player_gameweek_history_2022_23",
        "player_gameweek_history_2023_24",
    ]

    total_updated = 0
    total_not_found = 0

    for table_name in historical_tables:
        print(f"  - Processing {table_name}...")

        # Check if table exists and has a name column
        try:
            check_query = f"SELECT name FROM {table_name} LIMIT 1"
            execute_query(check_query)
        except Exception as e:
            print(f"    - Table {table_name} not accessible: {e}")
            continue

        # Get all unique player names from this table
        query = f"SELECT DISTINCT name FROM {table_name} WHERE name IS NOT NULL"
        results = execute_query(query)

        table_updated = 0
        table_not_found = 0

        for row in results:
            player_name = row[0]
            if player_name:
                standardized_name = convert_name(player_name)

                if standardized_name in all_players_mapping:
                    all_player_id = all_players_mapping[standardized_name]

                    # Update all records with this player name
                    update_query = f"""
                        UPDATE {table_name} 
                        SET all_player_id = %s 
                        WHERE name = %s
                    """
                    affected_rows = execute_command(update_query, (all_player_id, player_name))
                    table_updated += affected_rows
                else:
                    table_not_found += 1

        print(f"    - Updated: {table_updated}, Not found: {table_not_found}")
        total_updated += table_updated
        total_not_found += table_not_found

    print(f"  - Total updated: {total_updated}")
    print(f"  - Total not found: {total_not_found}")
    return total_updated, total_not_found


def main():
    """Main function to populate all foreign key relationships."""
    print("Starting foreign key population process...")

    try:
        # Get the mapping of standardized names to all_players IDs
        all_players_mapping = get_all_players_mapping()

        if not all_players_mapping:
            print("No players found in all_players table. Exiting.")
            return

        # Update each table
        players_updated, players_not_found = update_players_table(all_players_mapping)
        # season_updated, season_not_found = update_player_season_history(all_players_mapping)
        historical_updated, historical_not_found = update_historical_season_tables(
            all_players_mapping
        )

        # Summary
        print("\n" + "=" * 50)
        print("FOREIGN KEY POPULATION SUMMARY")
        print("=" * 50)
        print(f"Players table: {players_updated} updated, {players_not_found} not found")
        # print(
        #     f"Season history: {season_updated} records updated, {season_not_found} names not found"
        # )
        print(
            f"Historical seasons: {historical_updated} records updated, {historical_not_found} names not found"
        )
        print("=" * 50)

        print("\nForeign key population completed successfully!")

    except Exception as e:
        print(f"Error during foreign key population: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
