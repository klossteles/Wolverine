from celery.result import AsyncResult
from django.http import HttpResponse

import worker


def index(request, param):
    task = worker.wolverine_workers.some_long_processing.delay(param)
    return HttpResponse('Dispatch to workers. Task id: {}'.format(task.task_id))


def query_task(request, task_id):
    res = AsyncResult(task_id)
    if res.ready():
        return HttpResponse('Task ready: {}'.format(res.get()))
    else:
        return HttpResponse('The task is not ready yet')

