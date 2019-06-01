import os
import zipfile

from celery.result import AsyncResult
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

import worker
from userint.forms import UploadFileForm
from userint.utils import save_file
from wolverine import settings


@login_required
def cgne(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            from userint.models import SignalInput

            signal_input = SignalInput()
            signal_input.input_filename = save_file(request.FILES['file'])
            signal_input.owner = request.user
            signal_input.save()

            task = worker.wolverine_workers.process_with_cgne.delay(signal_input.id)
            message = 'The file is being processed with id: {}'.format(task.task_id)
        else:
            message = 'You must select a file'

        return render(request, 'cgne.html', {'form': form, 'message': message})
    else:
        form = UploadFileForm()
        return render(request, 'cgne.html', {'form': form})


@login_required
def cgne_details(request, signal_output_id):
    from userint.models import SignalOutput

    signal_output = SignalOutput.objects.get(pk=signal_output_id)
    if signal_output.signal_input.owner != request.user:
        return HttpResponseNotFound()

    return render(request, 'cgne_details.html', {'signal_output': signal_output})


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

    from userint.models import SignalInput
    signal_inputs = SignalInput.objects.filter(owner=request.user).prefetch_related()

    return render(request, 'dashboard.html', {
        'user': user,
        'signal_inputs': signal_inputs,
    })


@login_required
def image(request, task_id):
    image_filename = '{}.png'.format(task_id)
    with open(os.path.join(settings.BASE_DIR, image_filename), 'rb') as image_file:
        response = HttpResponse(image_file.read(), content_type='image/png')
        response['Content-Disposition'] = 'inline; filename=' + image_filename
        return response


@login_required
def download_images(request):
    field_names = [field_name for field_name in request.POST if 'signaloutput' in field_name]
    signal_output_ids = [signaloutput_id.split('_')[1] for signaloutput_id in field_names]
    print(signal_output_ids)

    from userint.models import SignalOutput
    signal_outputs = SignalOutput.objects.filter(pk__in=signal_output_ids)

    zip = zipfile.ZipFile('temp.zip', 'w')
    for signal_output in signal_outputs:
        zip.write('{}.png'.format(signal_output.output_filename))

    zip.close()

    with open('temp.zip', 'rb') as raw_zipfile:
        response = HttpResponse(raw_zipfile.read())
        response['Content-Disposition'] = u'attachment; filename={0}'.format('signal_output_bundle.zip')
        response['Content-Type'] = 'application/x-zip'
        return response
