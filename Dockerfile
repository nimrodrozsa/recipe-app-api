FROM python:3.7-alpine
LABEL org.opencontainers.image.authors="Acetech Development S.R.L."

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt //requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user