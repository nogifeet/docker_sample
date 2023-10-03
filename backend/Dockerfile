# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Create and set the working directory
WORKDIR /app

# Create a "logs" directory within the app directory
RUN mkdir logs

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8080 for the Flask app
EXPOSE 8080

# Run the Flask app
CMD ["python3", "./app.py"]
