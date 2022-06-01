#!/bin/sh

. venv/bin/activate
export FLASK_APP=init.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5001