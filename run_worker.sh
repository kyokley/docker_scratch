#!/bin/bash

# sleep 10

cd myproject

su -m myuser -c "celery worker -A myproject.tasks -Q default -n default@%h"
