#!/usr/bin/env bash
# Render runs this script during every deploy.
set -o errexit

pip install -r requirements.txt
pip install -r requirements-production.txt

python manage.py collectstatic --no-input
python manage.py migrate
