from celery.result import AsyncResult
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

import worker


@login_required
def index(request, param):
    task = worker.wolverine_workers.some_long_processing.delay(param)
    return HttpResponse('Dispatch to workers. Task id: {}'.format(task.task_id))


@login_required
def query_task(request, task_id):
    res = AsyncResult(task_id)
    if res.ready():
        return HttpResponse('Task ready: {}'.format(res.get()))
    else:
        return HttpResponse('The task is not ready yet')


@login_required
def cgne(request):
    task = worker.wolverine_workers.process_with_cgne.delay()
    return HttpResponse('Your image was dispatched to workers. Task id: {}'.format(task.task_id))


@login_required
def obtain_image(request, task_id):
    res = AsyncResult(task_id)
    if res.ready():
        return HttpResponse('The image was saved')
    else:
        return HttpResponse('The task is not ready yet')


@login_required
def dashboard(request):
    return HttpResponse('You are logged in!')
