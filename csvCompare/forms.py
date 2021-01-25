from django import forms
from .models import CSV_JiraDB


class CsvModelForm(forms.ModelForm):
    class Meta:
        model = CSV_JiraDB
        fields = ('file_name',)