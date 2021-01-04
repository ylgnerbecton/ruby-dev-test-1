FROM python:3.6.9-slim-stretch
LABEL maintainer Ylgner Becton <ylgner.becton@gmail.com>

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev libffi-dev git --no-install-recommends

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000
RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ADD . /app

CMD /app/manage.py migrate && /app/manage.py runserver 0.0.0.0:8000