from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from movies.models import Genre, Movie, Rental


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

        widgets = {
            'release_date': DatePickerInput()
        }
