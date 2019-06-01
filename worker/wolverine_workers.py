import matplotlib.pyplot as plt

from celery import Celery

from cgne import cgne

app = Celery('wolverine_workers', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')


@app.task()
def process_with_cgne(file_name):
    result = cgne.cgne(file_name)

    task_id = process_with_cgne.request.id
    plt.imsave('{}.png'.format(task_id), result)
