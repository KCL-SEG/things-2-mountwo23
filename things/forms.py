from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from things.models import Thing

class ThingForm(forms.ModelForm):
    """Form for Thing model."""

    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }