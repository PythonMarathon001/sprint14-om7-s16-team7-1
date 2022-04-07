from django import forms


class UserForm(form):
    name = forms.CharField(lable="Name")
    surname = forms.CharField(lable="surname")
    patronymic = forms.CharField(lable="patronymic")
