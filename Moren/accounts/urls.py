from django.urls import path, reverse_lazy
from . import views

from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit-profile/', views.EditProfileView.as_view(), name='edit_profile'),
    path('edit-profile/password',
         auth_views.PasswordChangeView.as_view(template_name="accounts/change_password.html", success_url=reverse_lazy('accounts:change_password_done')), name='change_password'),
    path('edit-profile/password/done', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/change_password_done.html'), name='change_password_done'),
]
