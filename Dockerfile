# Stage 1: Build stage
FROM python:3.11-slim as builder

WORKDIR /app

# Copy the project files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Stage 2: Runtime stage
FROM python:3.11-slim as runtime

WORKDIR /app

# Copy the built application and its dependencies from the builder stage
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Expose the port the app runs on
EXPOSE 8000