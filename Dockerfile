# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . .

# Expose the port on which FastAPI is running
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "main:app" "--host 0.0.0.0"]
