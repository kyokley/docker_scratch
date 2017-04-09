import time
import random
from celery import Celery

app = Celery('tasks', backend='rpc://', broker='amqp://admin:mypass@rabbit')

@app.task
def add(x, y):
    time.sleep(3)
    return x + y

if __name__ == '__main__':
    results = [add.delay(random.randint(0, 10),
                         random.randint(0, 10)) for x in range(100)]

    remaining = [result for result in results if not result.ready()]
    while remaining:
        time.sleep(1)
        print('%s remaining' % len(remaining))
        remaining = [result for result in results if not result.ready()]

    for result in results:
        print(result.result)
    print('done')
