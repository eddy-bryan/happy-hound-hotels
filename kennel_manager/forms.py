from django import forms
from .models import Booking, Review
from datetime import datetime, timedelta

class SearchForm(forms.Form):
    """
    Form for searching kennels.

    Attributes:
        NUM_PETS_CHOICES (list): List of tuples representing number of pets choices.
        today (datetime.date): Current date.
        tomorrow (datetime.date): Date representing tomorrow.
        after_tomorrow (datetime.date): Date representing the day after tomorrow.
    """

    # Define choices for number of pets
    NUM_PETS_CHOICES = [(i, str(i)) for i in range(1, 11)]

    # Calculate today's date and dates for tomorrow and the day after tomorrow
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    after_tomorrow = tomorrow + timedelta(days=1)

    # Define form fields
    check_in_date = forms.DateField(
        label='Check-in Date',
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/YYYY'}),
        input_formats=['%d/%m/%Y']
    )
    check_out_date = forms.DateField(
        label='Check-out Date',
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/YYYY'}),
        input_formats=['%d/%m/%Y']
    )
    num_pets = forms.ChoiceField(
        choices=NUM_PETS_CHOICES,
        label='Number of Pets',
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class BookingForm(forms.ModelForm):
    """
    Form for booking kennels.

    Attributes:
        NUM_PETS_CHOICES (list): List of tuples representing number of pets choices.
    """

    # Define choices for number of pets
    NUM_PETS_CHOICES = [(i, str(i)) for i in range(1, 11)]

    # Define form fields
    check_in_date = forms.DateField(
        label='Check-in Date',
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/YYYY'}),
        input_formats=['%d/%m/%Y']
    )
    check_out_date = forms.DateField(
        label='Check-out Date',
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/YYYY'}),
        input_formats=['%d/%m/%Y']
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
    """
    Form for submitting reviews.

    Attributes:
        model (class): Model for which the form is created.
        fields (tuple): Tuple of field names to include in the form.
    """
    class Meta:
        model = Review
        fields = (
            'body',
            )
