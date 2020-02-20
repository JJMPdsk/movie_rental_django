from django.db import models
from accounts.models import AppUser
from django.utils import timezone
from django.urls import reverse_lazy


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("movies:detail", kwargs={"pk": self.pk})


class Rental(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date_rented = models.DateTimeField(default=timezone.now)
    date_returned = models.DateTimeField(null=True, blank=True)
    customer = models.ForeignKey(AppUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"Movie: {self.movie.name}, Customer: {self.customer.user.username}"
