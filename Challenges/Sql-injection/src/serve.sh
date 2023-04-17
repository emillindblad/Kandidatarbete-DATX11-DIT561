#!/bin/sh
gunicorn 'app:app' \
    --bind '0.0.0.0:8001' \
    --workers 4 \
    --access-logfile "-" \
    --error-logfile "-"