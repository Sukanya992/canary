# Use Python 3.9 as base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose port
EXPOSE 5000

# Set the environment variable for version
ENV VERSION=old

# Run the application
CMD ["python", "app.py"]
