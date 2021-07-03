#!/bin/bash
echo "Pulling latest Code"
git pull
pid=`ps -ef | grep logger.py | grep -v grep | awk '{print $2}'`
echo "Killing the existing process......"
kill -15 $pid
echo "Restarting the logger application"
python3 logger.py
