#!/bin/bash
# cd /opt/bitnami/projects/SCUP/
# git pull
python3 /opt/bitnami/projects/SCUP/manage.py makemigrations
python3 /opt/bitnami/projects/SCUP/manage.py migrate
python3 /opt/bitnami/projects/SCUP/manage.py collectstatic --no-input
/opt/bitnami/projects/SCUP/deploy_scripts/logfix.sh
/opt/bitnami/projects/SCUP/deploy_scripts/restart.sh
