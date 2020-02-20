from django.urls import path, reverse_lazy
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieListView.as_view(), name='list'),
    path('<int:pk>', views.MovieDetailView.as_view(), name='detail'),
    path('<int:pk>/edit', views.MovieUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.MovieDeleteView.as_view(), name='delete'),
    path('create/', views.MovieCreateView.as_view(), name='create'),

    path('<int:pk>/rent', views.MovieRentView.as_view(), name='rent'),
    path('my', views.MovieMyListView.as_view(), name='my_list'),
    path('rental/<int:pk>/return', views.MovieReturnView.as_view(), name='return'),
]
