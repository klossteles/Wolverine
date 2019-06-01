from django.conf import settings
from django.db import models


class SignalInput(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    input_filename = models.FilePathField()


class SignalOutput(models.Model):
    signal_input = models.OneToOneField(SignalInput, on_delete=models.DO_NOTHING)

    output_filename = models.FilePathField()
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
    pixel_size = models.IntegerField()
    iteration_number = models.IntegerField()
