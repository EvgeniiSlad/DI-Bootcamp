from django import forms
from .models import *
from django.core.exceptions import ValidationError

def has_numbers(in_string:str):
    return any(char.isdigit() for char in in_string)


class AddFilmForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = ('__all__')

    def clean_first_name(self):
        name:str = self.cleaned_data.get('first_name')
        if has_numbers(name):
            raise ValidationError("can't include numbers in first name")
        return name 


class AddDirectorForm(forms.ModelForm):

    class Meta:
        model = Director
        fields = ('__all__')
        widgets = {
            'release_date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
        }