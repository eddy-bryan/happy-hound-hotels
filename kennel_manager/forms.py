from django import forms

class NumberInputWithPlaceholder(forms.NumberInput):
    input_type = 'number'

    def __init__(self, attrs=None, placeholder=None):
        super().__init__(attrs)
        if placeholder:
            self.attrs['placeholder'] = placeholder

class SearchForm(forms.Form):
    check_in_date = forms.DateField(label='Check-in Date', widget=forms.DateInput(attrs={'placeholder': 'Check-in date'}))
    check_out_date = forms.DateField(label='Check-out Date', widget=forms.DateInput(attrs={'placeholder': 'Check-out date'}))
    num_pets = forms.IntegerField(min_value=1, label='Number of Pets', widget=NumberInputWithPlaceholder(attrs={'placeholder': 'Number of pets'}))
