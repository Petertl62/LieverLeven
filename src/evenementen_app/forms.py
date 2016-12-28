from django import forms

from .models import Inschrijving


class ModelInschrijfForm(forms.ModelForm):
    class Meta:
        model = Inschrijving
        fields = [
            'voornaam', 'achternaam', 'email', 'telefoon', 'bericht',
        ]
