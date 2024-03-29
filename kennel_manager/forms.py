from django import forms

class SearchForm(forms.Form):
    check_in_date = forms.DateField(label='Check-in Date')
    check_out_date = forms.DateField(label='Check-out Date')
    num_pets = forms.IntegerField(min_value=1, label='Number of Pets')