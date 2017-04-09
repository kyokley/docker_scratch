#!/bin/bash

echo "Waiting for rabbit/redis to start up"
sleep 10
echo "Let's go!"

su -m myuser -c "python -u tasks.py"
