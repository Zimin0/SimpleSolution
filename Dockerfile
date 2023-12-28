FROM python:3.9

COPY ./simplesolution_project /app
WORKDIR /app

RUN pip install -r requirements.txt
