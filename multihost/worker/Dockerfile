FROM celery

ADD . /app/

WORKDIR /app/

CMD celery worker -A tasks -n default@%h
