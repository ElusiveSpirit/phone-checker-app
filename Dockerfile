FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN addgroup -S python \
    && adduser -S -G python python

RUN apk add --update --no-cache --virtual .build-deps \
        g++ \
        python3-dev \
        libxml2 \
        libxml2-dev && \
    apk add libxslt-dev

RUN pip install pipenv

COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock
RUN pipenv install --system --deploy

COPY . /app

USER python

WORKDIR /app
