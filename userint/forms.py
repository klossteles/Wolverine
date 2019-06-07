import django.forms


class UploadFileForm(django.forms.Form):
    file = django.forms.FileField()
    model_size = django.forms.ChoiceField(choices=[(3600, '60 x 60')])
