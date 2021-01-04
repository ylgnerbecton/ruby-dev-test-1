from django import forms

from apps.core.models import *


class FilesForm(forms.ModelForm):
    path = forms.CharField(label='Diretório', max_length=250)
    sub_path = forms.CharField(label='Sub Diretório', max_length=250)

    class Meta:
        model = Files
        fields = ('name', 'upload',)
    
    def __init__(self, *args, **kwargs):
        super(FilesForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['upload'].widget.attrs['class'] = 'form-control'


