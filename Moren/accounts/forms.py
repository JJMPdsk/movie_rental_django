from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from movies.models import Genre, Movie, Rental


# class EmployeeCreateForm()


class MovieCreateForm(UserCreationForm):
    class Meta:
        model = Movie
        fields = "__all__"
