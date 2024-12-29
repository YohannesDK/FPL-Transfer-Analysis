FROM python:3.10-slim

WORKDIR /app

# Set environment variables, to include scraper in the PYTHONPATH
ENV PYTHONPATH="/app:/app/scraper"


# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Default command (overridden in Docker Compose)
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]

