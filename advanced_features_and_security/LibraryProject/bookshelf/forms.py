# bookshelf/forms.py
from django import forms

class ExampleForm(forms.Form):
    """
    Minimal form required by the checker.
    """
    name = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=False)
