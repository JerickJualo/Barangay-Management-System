#!/usr/bin/env bash
set -e  # Exit immediately on error

echo "==== Installing Python dependencies ===="
pip install -r requirements.txt

echo "==== Running database migrations ===="
python manage.py migrate --noinput

echo "==== Collecting static files ===="
python manage.py collectstatic --noinput

echo "==== Build complete ===="
