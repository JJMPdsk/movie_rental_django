from django.contrib import admin
from movies.models import Genre, Movie, Rental
from accounts.models import AppUser

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Rental)
admin.site.register(AppUser)
