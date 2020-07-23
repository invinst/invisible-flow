#!/usr/bin/env bash

pwd
python3 manage.py db upgrade --directory invisible_flow/migrations
#wc -l invisible_flow/
gunicorn invisible_flow.app:app