FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files first
COPY pyproject.toml uv.lock ./

# Install UV for faster dependency management
RUN pip install --no-cache-dir uv

# Install Python dependencies
RUN uv pip install --system --no-cache-dir -e .

# Copy the entire application
COPY . .

# Ensure entrypoint script has execute permissions
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

