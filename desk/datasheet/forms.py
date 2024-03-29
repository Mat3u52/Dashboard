from django import forms
from .models import Guideline, Comment


class GuideForm(forms.ModelForm):
    title = forms.CharField(help_text='maximum 250 characters', required=True)
    # version = forms.ChoiceField(help_text='your guideline version will be automatically increased')
    # version = forms.CharField(required=True)
    # text = forms.TextField(required=True)
    image = forms.ImageField(required=True)
    # status = forms.CharField(required=True)

    class Meta:
        model = Guideline
        fields = ['title', 'version', 'text', 'image', 'status',]

        VERSION_CHOICES = [tuple([x, x/5]) for x in range(1, 21)]

        widgets = {
            'version': forms.Select(choices=VERSION_CHOICES),
        }
        help_texts = {
            'version': 'your guideline version will be automatically increased',
        }


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body',)

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control'}),
        #     'body': forms.Textarea(attrs={'class': 'form-control'})
        # }
