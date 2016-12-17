from django import forms

from .models import Inschrijving


class ModelInschijfForm(forms.ModelForm):
    class Meta:
        model = Inschrijving
        fields = [
            'voornaam', 'achternaam', 'email', 'telefoon', 'bericht',
        ]
