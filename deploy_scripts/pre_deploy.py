#!/usr/bin/env python3
"""Configures SCUP for a new deployment, clearing the path at SCUP_INSTALL_PATH.
"""

import os
import shutil
import subprocess

SCUP_INSTALL_PATH = "/opt/bitnami/projects/SCUP/"

def clear_install_path():
    """Forcefully removes all contents located at the SCUP_INSTALL_PATH so a new
    SCUP version can be installed.
    """
    if not os.path.exists(SCUP_INSTALL_PATH):
        print(f"'{SCUP_INSTALL_PATH}' does not currently exist on the system - no pre-deploy step needs to be executed.")  # TODO how do you log this properly to CloudWatch, logging?
    try:
        shutil.rmtree(SCUP_INSTALL_PATH)
    except Exception as e:
        print(f"Failed to clear '{SCUP_INSTALL_PATH}' because: {str(e)}")

def update_packages():
    """Wrapper to run 'sudo apt-get update' and 'sudo apt-get upgrade
    """
    # sudo apt-get update
    try:
        subprocess.check_call(["sudo", "apt-get", "update"])
    except Exception as e:
        print(f"Failed to run 'apt-get update' because: {str(e)}")
    # sudo apt-get upgrade
    try:
        subprocess.check_call(["sudo", "apt-get", "upgrade"])
    except Exception as e:
        print(f"Failed to run 'apt-get upgrade' because: {str(e)}")

if __name__ == "__main__":
    clear_install_path()