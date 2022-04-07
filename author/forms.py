from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
    name = forms.CharField(label="Name")
    surname = forms.CharField(label="Surname")
    patronymic = forms.CharField(label="Patronymic")

    class Meta:
        model = Author
        fields = ("name", "surname", "patronymic")
