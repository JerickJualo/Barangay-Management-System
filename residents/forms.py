# residents/forms.py
from django import forms
from .models import Resident

class ResidentForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    sex = forms.ChoiceField(choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
    ])
    civil_status = forms.ChoiceField(choices=[
        ('Married', 'Married'),
        ('Single', 'Single'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ])

    class Meta:
        model = Resident
        fields = [
            'name', 'birthdate', 'sex', 'civil_status',
            'contact_number', 'occupation', 'household'
        ]
