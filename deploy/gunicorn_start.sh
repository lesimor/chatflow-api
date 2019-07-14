#!/usr/bin/env bash
# You must execute in project root directory
source /venv/bin/activate
gunicorn -c /deploy/gunicorn/config.py api.wsgi:application