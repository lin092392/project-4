#Creating our Docker image using Python 3
FROM python:3

#Setting up the working directory to /api
WORKDIR /api

#Copying the current directory to
ADD . /api

#Getting the installbase ready
RUN pip install Flask

#Exposing the port 5000
EXPOSE 5000

# Environmnet Variable Definition
ENV STAGE 'dev'

#Launching api.py with the system startup
CMD ["python", "api.py"]
