# Use the official Python image as the base image
#FROM python:3.8

# Install system dependencies
#RUN apt-get update && apt-get install -y \
    #libpq-dev \
    #gcc

# Copy Flask application code into the Docker image
#COPY src/ /app

# Set the working directory to /app
#WORKDIR /app

# Install Python packages
#COPY requirements.txt /app/requirements.txt
#RUN pip install -r requirements.txt

# Set environment variables
#ENV FLASK_APP=app.py
#ENV FLASK_ENV=development
#ENV FLASK_RUN_PORT=5000

# Expose port 5000 to the host system
#EXPOSE 5000

# Specify the command to run when the Docker container starts
#CMD ["flask", "run", "--host=0.0.0.0"]

FROM python:3.10-buster

RUN apt-get update && apt-get install -y \
    man \
    groff

WORKDIR /app
COPY /src /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLAG=flag{default_flag}

CMD /bin/sh -c "echo \"${FLAG}\" > /app/flag.txt && flask run"


