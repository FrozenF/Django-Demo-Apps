# portfolio/forms.py

from django import forms
from .models import PortofolioItem

class PortofolioItemForm(forms.ModelForm):
    class Meta:
        model = PortofolioItem
        fields = ['title', 'description', 'image', 'link']