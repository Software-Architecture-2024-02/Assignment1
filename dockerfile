FROM python:3.11.4-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /bookstore

COPY . /bookstore/

COPY ./requirements.txt /bookstore/
RUN pip install -r requirements.txt