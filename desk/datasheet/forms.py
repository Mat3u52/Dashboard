from django import forms
from .models import Guideline


class GuideForm(forms.ModelForm):
    title = forms.CharField(help_text='maximum 250 characters')

    class Meta:
        model = Guideline
        fields = ['title', 'version', 'text', 'image',]

    # class SearchForm(forms.Form):
    #     query = forms.CharField()


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)
