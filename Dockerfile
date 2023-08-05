# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the app into the container
COPY . .

# Install the Python dependencies
RUN pip install -r requirements.txt


# Expose the port on which FastAPI is running
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
