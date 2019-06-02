import os
from datetime import datetime

import matplotlib.pyplot as plt
from celery import Celery

from cgne import cgne
from userint import utils

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wolverine.settings')

app = Celery('wolverine_workers', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')
app.config_from_object('django.conf:settings')


@app.task()
def process_with_cgne(signal_input_id):
    from userint.models import SignalInput, SignalOutput

    started_at = datetime.now()

    signal_input = SignalInput.objects.get(pk=signal_input_id)

    result, iteration_qty, size_in_pixels = cgne.cgne(signal_input.input_filename)

    task_id = process_with_cgne.request.id
    username = signal_input.owner.username

    output_filename = os.path.join(utils.userpath(username), '{}.png'.format(task_id))
    plt.imsave(output_filename, result)

    signal_output = SignalOutput()
    signal_output.signal_input = signal_input
    signal_output.output_filename = output_filename
    signal_output.started_at = started_at
    signal_output.finished_at = datetime.now()
    signal_output.iteration_number = iteration_qty
    signal_output.pixel_size = size_in_pixels
    signal_output.save()
