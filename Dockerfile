# Use the official Python 3.8 slim-buster image as the base image
FROM python:3.8-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements_dev.txt

# Set Airflow environment variables
ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW_VERSION=2.9.2


# Install Airflow
RUN pip install "apache-airflow==${AIRFLOW_VERSION}"

# Initialize the Airflow database
RUN airflow db init

RUN airflow users create -p admin -u admin

# Expose the Airflow web server port
EXPOSE 8080

# Start Airflow web server and scheduler
CMD ["sh", "-c", "airflow webserver & airflow scheduler"]
