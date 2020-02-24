from braces.views import GroupRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from Moren.settings import Roles
from movies.models import Genre


class GenreCreateView(GroupRequiredMixin, CreateView):
    group_required = [Roles.admin]
    model = Genre
    template_name = "genres/genre_create.html"
    success_url = reverse_lazy('genres:list')
    fields = '__all__'


class GenreListView(GroupRequiredMixin, ListView):
    group_required = [Roles.admin]
    model = Genre
    template_name = "genres/genre_list.html"
