from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Mete:
        model= Book
        fields = ['title', 'author']