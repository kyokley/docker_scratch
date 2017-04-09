import time
import random
from celery import Celery
from local_settings import IP_ADDR

AMQP_URL = 'amqp://admin:mypass@{}'.format(IP_ADDR)
app = Celery('tasks', backend='rpc://', broker=AMQP_URL)

@app.task
def add(x, y):
    time.sleep(3)
    return x + y

if __name__ == '__main__':
    results = [add.delay(random.randint(0, 10),
                         random.randint(0, 10)) for x in range(1000)]

    remaining = [result for result in results if not result.ready()]
    while remaining:
        time.sleep(1)
        print('%s remaining' % len(remaining))
        remaining = [result for result in results if not result.ready()]

    for result in results:
        print(result.result)
    print('done')
