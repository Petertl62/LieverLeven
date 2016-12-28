from django import forms

from .models import Haiku


class ModelHaikuForm(forms.ModelForm):
    class Meta:
        model = Haiku
        fields = [
            'title', 'line_one', 'line_two', 'line_three', 'text',
        ]
