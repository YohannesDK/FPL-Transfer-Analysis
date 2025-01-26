FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . /app

ENV PYTHONPATH=/app

CMD ["python", "/app/src/scheduler.py"]

# CMD ["echo", "Hello, World!"]
