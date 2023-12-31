#!/usr/bin bash

echo "Selenium Download API"
gunicorn --b 0.0.0.0:8080 -t 120 --log-level critical main:app