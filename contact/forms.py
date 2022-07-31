from django import forms
from django.forms import ModelForm, Textarea, TextInput, widgets, EmailInput
from .models import Contact, Subscribe


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'subject': TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': '5'}),
        }

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }