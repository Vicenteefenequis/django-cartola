#!/bin/bash

pipenv install
pipenv run python manage.py migrate

tail -f /dev/null