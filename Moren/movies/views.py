from os.path import exists

from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (
    CreateView, DeleteView, DetailView, FormView, ListView, RedirectView,
    UpdateView)

from accounts.models import AppUser
from Moren.settings import Roles
from movies.forms import MovieCreateForm
from movies.models import Genre, Movie, Rental


class MovieCreateView(GroupRequiredMixin, CreateView):
    group_required = [Roles.admin, Roles.employee]

    model = Movie
    form_class = MovieCreateForm
    template_name = "movies/movie_create.html"


class MovieListView(LoginRequiredMixin, ListView):
    model = Movie
    template_name = "movies/movie_list.html"


class MovieDeleteView(GroupRequiredMixin, DeleteView):
    group_required = [Roles.admin, Roles.employee]

    model = Movie
    template_name = "movies/movie_delete.html"
    success_url = reverse_lazy('movies:list')


class MovieDetailView(LoginRequiredMixin, DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"


class MovieUpdateView(GroupRequiredMixin, UpdateView):
    group_required = [Roles.admin, Roles.employee]

    model = Movie
    fields = '__all__'
    template_name = "movies/movie_update.html"

    def get_form(self):
        form = super().get_form()
        form.fields['release_date'].widget = DatePickerInput()
        return form


class MovieRentView(GroupRequiredMixin, RedirectView):
    group_required = Roles.customer

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('movies:my_list')

    def get(self, request, *args, **kwargs):

        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        customer = AppUser.objects.get(user_id=self.request.user.id)

        # check whether customer rents the movie already, which isn't returned
        if Rental.objects.filter(customer=customer, movie=movie, date_returned__isnull=True).exists():
            messages.warning(
                self.request, "You can't rent this movie. Please return it first.")
        else:
            if movie.quantity > 0:
                Rental.objects.create(customer=customer, movie=movie)
                movie.quantity -= 1
                movie.save()
            else:
                messages.warning(self.request, "Movie quantity too low")

        return super().get(request, *args, **kwargs)


class MovieMyListView(GroupRequiredMixin, ListView):
    group_required = Roles.customer
    model = Rental
    template_name = "movies/movie_my_list.html"

    def get_queryset(self):
        customer = get_object_or_404(AppUser, user_id=self.request.user.id)
        return super().get_queryset().filter(customer=customer).order_by('-date_rented')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["returned_list"] = context['rental_list'].filter(
            date_returned__isnull=False)
        context["unreturned_list"] = context['rental_list'].filter(
            date_returned__isnull=True)
        return context


class MovieReturnView(GroupRequiredMixin, RedirectView):
    group_required = Roles.customer

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('movies:my_list')

    def get(self, request, *args, **kwargs):
        rental = Rental.objects.get(pk=self.kwargs.get('pk'))

        rental.date_returned = timezone.now()
        rental.movie.quantity += 1

        rental.movie.save()
        rental.save()

        return super().get(request, *args, **kwargs)
