from django.forms import ModelForm, TextInput, Textarea
from .models import *


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'subject': TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': '5'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'form-control'})

