FROM python:3.8-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY run-requirements.txt /usr/src/app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
