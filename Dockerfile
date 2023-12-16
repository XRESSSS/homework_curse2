FROM python:3.11.6-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get upgrade

COPY . .

CMD ["python", "homework5"]
