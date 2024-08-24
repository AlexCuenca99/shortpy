# pull official base image
FROM python:3.11

# Packages
RUN apt-get update

# set work directory
WORKDIR /usr/src/app
EXPOSE 5000

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY ./src /usr/src/app/