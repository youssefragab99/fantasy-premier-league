FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir psycopg[binary]==3.2.1

COPY scripts ./scripts

CMD ["python", "-u", "scripts/db_check.py"]

