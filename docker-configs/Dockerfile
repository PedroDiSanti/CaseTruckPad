FROM python:3.6
LABEL maintainer="Pedro Di Santi <pedroa.disanti@gmail.com>"
RUN apt-get update
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_ENV="docker"
EXPOSE 5000