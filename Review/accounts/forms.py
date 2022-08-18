from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import contact


class Contact(forms.ModelForm):
    class Meta:
        model = contact
        #itme ko every model lai mapping gernae
        fields = "__all__"