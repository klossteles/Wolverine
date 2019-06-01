import os

from celery.result import AsyncResult
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

import worker
from wolverine import settings


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
    user = request.user
    image_url = reverse('image', kwargs={'task_id': 'aa4dae91-8f98-4715-885b-fb7cc7955456'})

    return render(request, 'dashboard.html', {
        'user': user,
        'image_url': image_url,
    })


@login_required
def image(request, task_id):
    image_filename = '{}.png'.format(task_id)
    with open(os.path.join(settings.BASE_DIR, image_filename), 'rb') as image_file:
        response = HttpResponse(image_file.read(), content_type='image/png')
        response['Content-Disposition'] = 'inline; filename=' + image_filename
        return response
