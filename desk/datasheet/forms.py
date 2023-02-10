from django import forms
from .models import Guideline


class ImgForm(forms.ModelForm):
    class Meta:
        model = Guideline
        fields = ['image']