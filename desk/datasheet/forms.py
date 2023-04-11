from django import forms
from .models import Guideline, Comment


class GuideForm(forms.ModelForm):
    title = forms.CharField(help_text='maximum 250 characters')

    class Meta:
        model = Guideline
        fields = ['title', 'version', 'text', 'image',]


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        filter = ('name', 'email', 'body')
