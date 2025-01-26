FROM python:3.10-slim

WORKDIR /app

# Set PYTHONPATH to include both the backend and scraper
ENV PYTHONPATH="/app:/app/scraper"

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Default command
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
