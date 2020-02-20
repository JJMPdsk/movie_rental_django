from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = "accounts/register.html"


class EditProfileView(UpdateView):
    fields = ['first_name', 'last_name']
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user
