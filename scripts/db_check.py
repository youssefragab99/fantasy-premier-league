import importlib
import os
import sys
import time


def build_database_url() -> str:
    env_url = os.getenv("DATABASE_URL")
    if env_url:
        return env_url

    user = os.getenv("POSTGRES_USER", "fpl")
    password = os.getenv("POSTGRES_PASSWORD", "fplpassword")
    host = os.getenv("DB_HOST", "db")
    port = os.getenv("DB_PORT", "5433")
    db = os.getenv("POSTGRES_DB", "fpldb")
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"


def wait_and_connect(database_url: str, timeout_seconds: int = 60) -> int:
    deadline = time.time() + timeout_seconds
    last_error: Exception | None = None
    try:
        psycopg = importlib.import_module("psycopg2")  # type: ignore[assignment]
    except ModuleNotFoundError:
        print(
            "psycopg2 is required. Run inside Docker or install 'psycopg2-binary'.",
            file=sys.stderr,
        )
        return 2
    error_cls = getattr(psycopg, "Error", Exception)
    while time.time() < deadline:
        try:
            with psycopg.connect(database_url) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
                    cursor.fetchone()
            print("Connected to Postgres and executed SELECT 1 successfully.")
            return 0
        except error_cls as exc:  # type: ignore[misc]
            last_error = exc
            time.sleep(1.5)

    print(f"Failed to connect to Postgres within {timeout_seconds}s: {last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(wait_and_connect(build_database_url()))
