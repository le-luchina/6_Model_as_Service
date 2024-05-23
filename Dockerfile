# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Copy the rest of your application code into the container
COPY . .

#working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 8000

# Run the Flask server
CMD ["python", "/app/server.py"]
