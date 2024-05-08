#!/usr/bin/env python3
"""Provides interactions with the 'ctlscript.sh' and Apache for SCUP.
"""

import argparse
import subprocess

CTLSCRIPT_SH = "/opt/bitnami/ctlscript.sh"
VALID_ARGS = ("start", "stop", "status", "restart")

def stop_apache():
    """Stops the Apache process that runs SCUP
    """
    try:
        subprocess.check_call(["sudo", CTLSCRIPT_SH, "stop", "apache"])
    except Exception as e:
        print(f"Failed to stop Apache because: {str(e)}")

def start_apache():
    """Starts the Apache process that runs SCUP
    """
    try:
        subprocess.check_call(["sudo", CTLSCRIPT_SH, "start", "apache"])
    except Exception as e:
        print(f"Failed to start Apache because: {str(e)}")

def status_apache():
    """Statuses the Apache process that runs SCUP
    """
    try:
        subprocess.check_call([CTLSCRIPT_SH, "status", "apache"])
    except Exception as e:
        print(f"Failed to status Apache because: {str(e)}")

def restart_apache():
    """Restarts the Apache process that runs SCUP
    """
    stop_apache()
    start_apache()
    status_apache()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('action', type=str, choices=VALID_ARGS, description=f"Action to be called, must be one of: {', '.join(VALID_ARGS)}")
    args = parser.parse_args()

    if args.action.lower() == "start":
        start_apache()
    elif args.action.lower() == "stop":
        stop_apache()
    elif args.action.lower() == "status":
        status_apache()
    elif args.action.lower() == "restart":
        restart_apache()