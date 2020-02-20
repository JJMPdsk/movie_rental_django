from django.shortcuts import render, get_object_or_404
from movies.models import Movie, Rental, Genre
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView, FormView, RedirectView
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput
from django.urls import reverse_lazy
from movies.forms import MovieRentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from accounts.models import AppUser


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = '__all__'
    template_name = "movies/movie_create.html"

    def get_form(self):
        form = super().get_form()
        form.fields['release_date'].widget = DatePickerInput()
        return form


class MovieListView(ListView):
    model = Movie
    template_name = "movies/movie_list.html"


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = "movies/movie_delete.html"
    success_url = reverse_lazy('movies:list')


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = '__all__'
    template_name = "movies/movie_update.html"

    def get_form(self):
        form = super().get_form()
        form.fields['release_date'].widget = DatePickerInput()
        return form


class MovieRentView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('movies:list')

    def get(self, request, *args, **kwargs):

        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))

        if movie.quantity > 0:
            customer = AppUser.objects.get(user_id=self.request.user.id)
            Rental.objects.create(customer=customer, movie=movie)
            movie.quantity -= 1
            movie.save()
        else:
            messages.warning(self.request, "Movie quantity too low")

        return super().get(request, *args, **kwargs)

# class MovieMyListView(LoginRequiredMixin, ListView):
#     model = Movie
#     template_name = "movies/movie_list.html"

#     def get_queryset(self):
#         user = get_object_or_404
#         return super().get_queryset().filter(customer=self.request.user)
