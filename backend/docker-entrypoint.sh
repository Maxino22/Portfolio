#!/bin/sh

echo "Waiting for Postgres to start..."
./wait-for db:5432

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000