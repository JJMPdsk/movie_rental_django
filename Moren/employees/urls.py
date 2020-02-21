from django.urls import path, reverse_lazy
from employees import views

app_name = 'employees'

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='list'),
    path('create', views.EmployeeCreateView.as_view(), name='create'),
    path('<int:pk>/delete', views.EmployeeDeleteView.as_view(), name='delete'),
    path('<int:pk>/details', views.EmployeeDetailView.as_view(), name='detail'),
]
