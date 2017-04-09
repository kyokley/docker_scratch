FROM python:2.7

ADD . /app/

WORKDIR /app/

RUN pip install -r requirements.txt

CMD celery worker -A tasks -n default@%h --loglevel=INFO
