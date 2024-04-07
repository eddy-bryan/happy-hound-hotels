from django import forms
from .models import Booking
from account_management.models import PetProfile

class NumberInputWithPlaceholder(forms.NumberInput):
    input_type = 'number'

    def __init__(self, attrs=None, placeholder=None):
        super().__init__(attrs)
        if placeholder:
            self.attrs['placeholder'] = placeholder


class SearchForm(forms.Form):
    NUM_PETS_CHOICES = [(i, str(i)) for i in range(1, 11)]

    check_in_date = forms.DateField(
        label='Check-in Date',
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'MM/DD/YYYY'})
    )
    check_out_date = forms.DateField(
        label='Check-out Date',
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'MM/DD/YYYY'})
    )
    num_pets = forms.ChoiceField(
        choices=NUM_PETS_CHOICES,
        label='Number of Pets',
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date', 'pet_name']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'MM/DD/YYYY'}),
            'check_out_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'MM/DD/YYYY'}),
            'pet_name': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pet_name'].queryset = PetProfile.objects.filter(owner=user)
