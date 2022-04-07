from django import forms
from .models import Book


class SearchForm(forms.Form):
    search = forms.CharField(label="search")


class BookForm(forms.ModelForm):
    name = forms.CharField(label="Name")
    description = forms.CharField(label="description", widget=forms.widgets.Textarea())
    count = forms.IntegerField(widget=forms.widgets.TextInput(attrs={'value': 10}))
    authors = forms.ModelMultipleChoiceField

    class Meta:
        model = Book
        fields = ("name", "description", "count", "authors")
