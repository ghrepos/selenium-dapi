#!/usr/bin bash

gunicorn --bind 0.0.0.0:7860 server.flask:app