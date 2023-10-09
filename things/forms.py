"""Forms of the project."""
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from things.models import Thing


# Create your forms here.

class ThingForm(forms.ModelForm):
    """Form for Thing model."""
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
    name = forms.CharField(max_length=35)
    description = forms.CharField(max_length=120)
    quantity = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )