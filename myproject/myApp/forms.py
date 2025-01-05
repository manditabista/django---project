from django import forms
from .models import Book

class BookForm(forms.Form):
    bk_name = forms.CharField()
    bk_number = forms.IntegerField()