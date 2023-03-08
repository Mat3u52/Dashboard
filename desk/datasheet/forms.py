from django import forms
from .models import Guideline


class GuideForm(forms.ModelForm):
    title = forms.CharField(help_text='maximum 250 characters')

    class Meta:
        model = Guideline
        fields = ['title', 'version', 'text', 'image',]
