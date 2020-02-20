from django import forms
from movies.models import Rental, Movie, Genre
from bootstrap_datepicker_plus import DateTimePickerInput


class MovieRentForm(forms.ModelForm):

    class Meta:
        model = Rental
        fields = ('customer', 'movie', 'date_rented')

        widgets = {
            'date_rented': DateTimePickerInput()
        }
