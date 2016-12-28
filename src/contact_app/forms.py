from django import forms

from .models import Contact


class ModelContactForm(forms.ModelForm):
    street = forms.CharField(max_length=64, required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Hoofdstraat 1',
        }))
    zipcode = forms.CharField(max_length=32, required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '1234 AB',
        }))
    city = forms.CharField(max_length=256, required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Amsterdam',
        }))
    country = forms.CharField(max_length=32, required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nederland',
        }))
    phonenumber = forms.CharField(max_length=16, required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '+31 6 12345678',
        }))

    class Meta:
        model = Contact
        fields = [
            'firstname', 'lastname', 'street', 'zipcode', 'city', 'country',
            'email', 'birthday', 'gender', 'company', 'phonenumber', 'title',
            'content',
        ]
        widgets = {
            'firstname': forms.TextInput(attrs={
                'placeholder': 'John',
            }),
            'lastname': forms.TextInput(attrs={
                'placeholder': 'Smith',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'johnsmith@gmail.com',
            }),
            'birthday': forms.DateInput(attrs={
                'placeholder': '23/10/2006',
            }),
            'gender': forms.Select(),
            'company': forms.TextInput(attrs={
                'placeholder': 'Bedrijf inc.',
            }),
            'title': forms.TextInput(attrs={
                'placeholder': 'Mijn Bericht',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Hallo, ik heb je website gezien en...',
            }),
        }
