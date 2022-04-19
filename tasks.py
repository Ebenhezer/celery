from celery import Celery
from time import sleep
app = Celery('tasks', backend='rpc://', broker='amqp://guest@localhost//')

@app.task
def reverse(text):
    return text[::-1]

@app.task
def gen_prime(x):
    multiples = []
    results = []
    y = x + 1

    for i in range(2, y):
        if i not in multiples:
            results.append(i)
            for j in range(i*i, y, i):
                multiples.append(j)
    
    return results