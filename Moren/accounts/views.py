from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from accounts.models import AppUser
from Moren.settings import Roles


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register.html"

    # override default registration behaviour
    def form_valid(self, form):
        self.object = form.save()

        group = Group.objects.get(name=Roles.customer)
        self.object.groups.add(group)
        self.object.save()

        AppUser.objects.create(user_id=self.object.id)

        return HttpResponseRedirect(reverse_lazy('accounts:login'))


class EditProfileView(UpdateView):
    fields = ['first_name', 'last_name']
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user
