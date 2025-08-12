import io

import polars as pl
import requests
from chardet import detect

from fantasy_premier_league.database import get_database_url


class FileLoader:
    def __init__(self, url: str | None = None):
        self.url = url

    def load_file(self) -> pl.DataFrame:
        """Load a file from GitHub and return a Polars DataFrame.

        Returns
        -------
        pl.DataFrame
            The loaded Polars DataFrame.
        Raises
        ------
        ValueError
            If no URL is provided.
        requests.RequestException
            If the file cannot be downloaded.
        """
        if not self.url:
            raise ValueError("No URL provided. Set url in constructor or use load_file_from_url method.")
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()

            # Detect the actual encoding of the file
            detected_encoding = detect(response.content)
            print(f"Detected encoding: {detected_encoding}")
            # Decode with the detected encoding, then encode as UTF-8
            encoding = detected_encoding["encoding"] if detected_encoding["encoding"] is not None else "utf-8"
            text_content = response.content.decode(encoding)

            # Load into Polars using StringIO
            df = pl.read_csv(io.StringIO(text_content))
            return df
        except requests.RequestException as e:
            raise requests.RequestException(f"Failed to download file from {self.url}: {e}") from e
        except Exception as e:
            raise RuntimeError(f"Failed to process file from {self.url}: {e}") from e

    def get_column_names_and_types(self) -> dict[str, str]:
        """Get the column names and types of a Polars DataFrame.

        Returns
        -------
        dict[str, str]
            Dictionary mapping column names to their Polars data types.
        """
        schema = self.load_file().schema
        return {name: str(dtype) for name, dtype in schema.items()}

    def generate_alembic_migration_table(self, table_name: str) -> str:
        """Generate an Alembic migration table creation code from column schema.

        Parameters
        ----------
        table_name : str
            The name of the table to create.
        schema : dict[str, str]
            Dictionary mapping column names to their Polars data types.

        Returns
        -------
        str
            The Alembic table creation code as a string.
        """
        # Map Polars types to SQLAlchemy types
        type_mapping = {
            "Int64": "sa.BigInteger()",
            "Int32": "sa.Integer()",
            "Int16": "sa.SmallInteger()",
            "Int8": "sa.SmallInteger()",
            "Float64": "sa.Float()",
            "Float32": "sa.Float()",
            "String": "sa.String()",
            "Utf8": "sa.String()",
            "Boolean": "sa.Boolean()",
            "Date": "sa.Date()",
            "Datetime": "sa.DateTime()",
            "Time": "sa.Time()",
        }

        # Start building the migration code
        lines = [
            "def upgrade():",
            f"    op.create_table('{table_name}',",
            "        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),",
        ]

        # Add columns based on schema
        for col_name, col_type in self.get_column_names_and_types().items():
            # Get the base type name (remove any parameters)
            base_type = str(col_type).split("(")[0]

            # Map to SQLAlchemy type
            sa_type = type_mapping.get(base_type, "sa.String()")

            # Add the column definition
            lines.append(f"        sa.Column('{col_name}', {sa_type}),")

        # Close the table definition
        lines.append("    )")
        lines.append("")
        lines.append("def downgrade():")
        lines.append(f"    op.drop_table('{table_name}')")

        return "\n".join(lines)


class DbFileLoader(FileLoader):
    pass

    def load_file_from_url(self, url: str) -> pl.DataFrame:
        """Load a file from a specific URL and return a Polars DataFrame.

        Parameters
        ----------
        url : str
            The URL of the file to load.

        Returns
        -------
        pl.DataFrame
            The loaded Polars DataFrame.
        """
        # Temporarily set the URL and load the file
        original_url = self.url
        self.url = url
        try:
            df = super().load_file()
        finally:
            self.url = original_url
        return df

    def write_file_to_db(self, season_name: str) -> None:
        """Write a Polars DataFrame to the database.

        Parameters
        ----------
        season_name : str
            The name of the season to write the DataFrame to.
        Raises
        ------
        RuntimeError
            If the database operation fails.
        """
        try:
            url = f"https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/{season_name}/gws/merged_gw.csv"
            df = self.load_file_from_url(url)
            df.write_database(
                table_name=f"player_gameweek_history_{season_name.replace('-', '_')}",
                connection=get_database_url(),
                if_table_exists="replace",
            )
            print(f"Successfully loaded {season_name} data to database")
        except Exception as e:
            raise RuntimeError(f"Failed to write {season_name} data to database: {e}") from e


seasons = ["2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]

if __name__ == "__main__":
    fl = DbFileLoader()
    for season in seasons:
        fl.write_file_to_db(season)
