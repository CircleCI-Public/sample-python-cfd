FROM python:3.8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y netcat

COPY run-requirements.txt /usr/src/app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]