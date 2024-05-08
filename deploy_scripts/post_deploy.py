#!/usr/bin/env python3
"""Configures SCUP after a new deployment.
"""

import sys
import subprocess

SCUP_INSTALL_PATH = "/opt/bitnami/projects/SCUP/"
PYTHON_REQUIREMENTS = "/opt/bitnami/projects/SCUP/requirements.txt"
MANAGE_PY = "/opt/bitnami/projects/SCUP/manage.py"
DJANGO_LOG_DIR = "/opt/bitnami/projects/SCUP/logs"
LOG_PERMS_OCTAL = "660"

def install_dependencies():
    """Runs a pip install for all required Python libraries.
    """
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", PYTHON_REQUIREMENTS])
    except Exception as e:
        print(f"Failed to install Python dependencies because: {str(e)}")

def setup_django_db():
    """Runs django commands from manage.py to setup Django's database for use.
    """
    # python3 manage.py makemigrations
    try:
        subprocess.check_call([sys.executable, MANAGE_PY, "makemigrations"])
    except Exception as e:
        print(f"Failed to run 'makemigrations' for Django because: {str(e)}")
    # python3 manage.py migrate
    try:
        subprocess.check_call([sys.executable, MANAGE_PY, "migrate"])
    except Exception as e:
        print(f"Failed to run 'migrate' for Django because: {str(e)}")
    # python3 manage.py collectstatic --no-input
    try:
        subprocess.check_call([sys.executable, MANAGE_PY, "collectstatic", "--no-input"])
    except Exception as e:
        print(f"Failed to run 'collectstatic' for Django because: {str(e)}")
    
def fix_logging_perms():
    """Establishes the correct permissions for the DJANGO_LOG_DIR directory
    """
    # sudo chown bitnami:daemon ...
    try:
        subprocess.check_call(["sudo", "chown", "bitnami:daemon", f"{DJANGO_LOG_DIR}/*.log"])
    except Exception as e:
        print(f"Failed to run 'chown' on logs because: {str(e)}")
    # sudo chmod ...
    try:
        subprocess.check_call(["sudo", "chmod", LOG_PERMS_OCTAL, f"{DJANGO_LOG_DIR}/*.log"])
    except Exception as e:
        print(f"Failed to run 'chmod' on logs because: {str(e)}")

if __name__ == "__main__":
    install_dependencies()
    setup_django_db()
    fix_logging_perms()