# Use the official Python image as a parent image
FROM python:latest

# Set environment variables to prevent buffering and ensure Python outputs directly to terminal
ENV PYTHONUNBUFFERED 1

# Create and set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the required Python packages
RUN pip install -r requirements.txt

# Copy the entire project directory into the container
COPY . /app/

# Expose port 8000 for the Django development server
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
