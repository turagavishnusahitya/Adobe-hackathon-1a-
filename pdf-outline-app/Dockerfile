# Use official Python slim base image supporting linux/amd64
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Create input and output directories inside container
RUN mkdir -p /app/input /app/output

# Default command to run your app
CMD ["python", "app.py"]
