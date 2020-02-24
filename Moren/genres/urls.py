from django.urls import path, reverse_lazy
from genres import views

app_name = 'genres'

urlpatterns = [
    path('create', views.GenreCreateView.as_view(), name='create'),
    path('', views.GenreListView.as_view(), name='list')
]
