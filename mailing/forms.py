from cProfile import label
from tkinter import Widget
from django import forms

from .models import ContactData


class ContactDataForm(forms.ModelForm):

    class Meta:
        model = ContactData
        fields = ("email",)
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': "Type your email..."})
        }
        labels = {
            'email': ''
        }
