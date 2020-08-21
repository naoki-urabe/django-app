FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /django_app
WORKDIR /django_app

ADD requirements.txt /django_app/

RUN apk update && \
    apk add git && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apk add --virtual build-deps gcc python3-dev musl-dev &&\
    apk add postgresql-dev &&\
    pip install psycopg2 &&\
    apk del build-deps

ADD . /django_app/