#!/bin/sh
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput

if [ "$LOAD_SEED_DATA" = "1" ]; then
  python manage.py load_portfolio_seed
fi

exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers "${GUNICORN_WORKERS:-3}" --timeout "${GUNICORN_TIMEOUT:-60}"
