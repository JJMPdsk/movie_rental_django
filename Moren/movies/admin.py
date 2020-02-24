from django.contrib import admin
from movies.models import Genre, Movie, Rental

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Rental)
