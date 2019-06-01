import time

from celery import Celery

from cgne import cgne

app = Celery('wolverine_workers', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')


@app.task()
def process_with_cgne():
    cgne.cgne(process_with_cgne.request.id)
