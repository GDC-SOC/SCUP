#!/bin/bash
cd /opt/bitnami/projects/SCUP/
git pull
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --no-input
./logfix.sh
./restart.sh
