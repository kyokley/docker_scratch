import time
import random
from celery import Celery

app = Celery('tasks', backend='redis://redis', broker='pyamqp://rabbit')

@app.task
def add(x, y):
    time.sleep(3)
    return x + y

if __name__ == '__main__':
    results = [add.delay(random.randint(0, 10),
                         random.randint(0, 10)) for x in range(10)]

    while any([not result.ready() for result in results]):
        time.sleep(1)

    for result in results:
        print(result.result)
