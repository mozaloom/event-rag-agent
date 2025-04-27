# Use the official lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install build dependencies (if needed) and clear cache
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your app runs on (modify if different)
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command to run the application
CMD ["python", "app.py"]
