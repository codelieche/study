#!/bin/bash
NAME="tdd_django"
USER=USERNAME
WORKERS=2
DJANGODIR=/home/${USER}/sites/SITENAME
DJANGO_WSGI_MODULE=superlists.wsgi
PID_PATH=/tmp/gunicorn.${NAME}.pid

cd ${DJANGODIR}/source

exec ../virtualenv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name $NAME \
    --user $USER \
    --pid $PID_PATH \
    --workers $WORKERS \
    --bind=unix:/tmp/SITENAME.socket \
    --log-level=info \
    --access-logfile=${DJANGODIR}/logs/gunicorn.access.log \
    --error-logfile=${DJANGODIR}/logs/gunicorn.error.log \