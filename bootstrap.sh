#!/usr/bin/env bash

ls -al
python3 manage.py db upgrade --directory invisible_flow/migrations
#wc -l invisible_flow/
gunicorn invisible_flow.app:app