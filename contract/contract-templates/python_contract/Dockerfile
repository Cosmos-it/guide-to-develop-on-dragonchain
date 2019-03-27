FROM python:3.7.2-alpine3.9

WORKDIR /home/app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . .
