#!/bin/sh

until pg_isready -h db -p 5432 -U exam -d exam_db; do
  echo "Waiting for PostgreSQL to be ready..."
  sleep 2
done

flask db upgrade

exec gunicorn --bind 0.0.0.0:5000 --workers 4 --access-logfile - --error-logfile - app.wsgi:app