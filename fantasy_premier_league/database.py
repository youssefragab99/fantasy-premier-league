from __future__ import annotations

import os
from typing import Generator

import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


class Base(DeclarativeBase):
    pass


def get_database_url() -> str:
    env_url = os.getenv("DATABASE_URL")
    if env_url:
        return env_url
    # Fallback to local docker-compose exposed Postgres
    user = config["db"]["username"]
    password = config["db"]["password"]
    host = config["db"]["host"]
    port = config["db"]["port"]
    db = config["db"]["db"]
    # Use psycopg2 driver as per pyproject dependency
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"


engine = create_engine(get_database_url(), future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


def get_db_session() -> Generator:
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
