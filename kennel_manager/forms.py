from django import forms
from .models import Booking, Review
from datetime import datetime, timedelta

class SearchForm(forms.Form):
    NUM_PETS_CHOICES = [(i, str(i)) for i in range(1, 11)]
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    after_tomorrow = tomorrow + timedelta(days=1)

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

    class Meta:
        model = Booking  # Specify the model for the form
        fields = ['check_in_date', 'check_out_date', 'num_pets']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'body',
            'rating',
            )
