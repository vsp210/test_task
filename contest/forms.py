from django import forms
from .models import *


class ParticipantForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Name', 'class': 'form-control'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email', 'class': 'form-control'}))
    code = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 10, 'placeholder': 'Code', 'class': 'form-control'}))
    class Meta:
        model = Participant
        fields = ['name', 'email', 'code']
