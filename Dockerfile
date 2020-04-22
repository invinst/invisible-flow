# Documentation: https://docs.google.com/document/d/1l6WqJeAJ5oEI_M1axphUslyx-WLBywksv4HliWn78Dw/edit?usp=sharing

FROM postgres:12.2

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/venv/bin/:$PATH
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV ENVIRONMENT=docker
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

RUN apt update -y && \
    apt-get install -y python-pip && \
    apt-get install -y git && \
    apt-get install -y python3-dev && \
    apt-get install -y python3-venv && \
    apt-get install -y postgresql && \
    apt-get install -y python-psycopg2 && \
    apt-get install -y postgis && \
    apt-get install -y libpq-dev && \
    apt-get install -y vim

COPY ./requirements.txt /app/requirements.txt

RUN python3 -m venv venv && \
    . venv/bin/activate && \
    python3 -m pip install -r ./app/requirements.txt

COPY . /app

WORKDIR /app

RUN python3 -m venv venv && \
    . venv/bin/activate && \
    export FLASK_APP=app.py && \
    export ENVIRONMENT=development

USER root

RUN useradd invisible_flow_testing; echo "invisible_flow_testing:password"|chpasswd;

USER postgres

CMD initdb; pg_ctl -D /var/lib/postgresql/data start; createdb; echo "create user invisible_flow WITH login;" | psql; \
    echo "create user invisible_flow_testing WITH login;" | psql; echo "ALTER ROLE invisible_flow_testing SUPERUSER" | psql; \
    echo "CREATE DATABASE invisible_flow_testing;" | psql; echo "GRANT ALL PRIVILEGES ON DATABASE invisible_flow_testing TO invisible_flow_testing;" | psql; \
    echo "CREATE EXTENSION postgis;" | psql -U invisible_flow_testing; \
    service postgresql start; \
    echo "password" | su invisible_flow_testing; \
    psql invisible_flow_testing < schema.sql; \
    echo "ALTER TABLE data_allegation ADD COLUMN cr_id character varying(50);" | psql -U invisible_flow_testing; \
    cd invisible_flow; \
    flask run --host=0.0.0.0 --port=$PORT
