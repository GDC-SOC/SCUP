#!/bin/bash
sudo /opt/bitnami/ctlscript.sh stop apache
sleep 3
sudo /opt/bitnami/ctlscript.sh start apache
sleep 3
sudo /opt/bitnami/ctlscript.sh status
