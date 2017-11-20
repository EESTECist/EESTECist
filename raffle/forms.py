from django import forms
from raffle import models


class EntryForm(forms.ModelForm):
    class Meta:
        model = models.Entry
        fields = ["name", "image"]


class TextFileForm(forms.ModelForm):
    class Meta:
        model = models.TextFile
        fields = ["text_file"]
