# Runtime stage
FROM python:3.11-slim 
# as runtime

WORKDIR /app

# Copy the project files
# COPY requirements.txt .
ADD . /app
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# # Copy the entire project
# COPY . .
# Expose the port the app runs on
EXPOSE 8000