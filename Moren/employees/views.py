
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, RedirectView

from accounts.models import AppUser
from Moren.settings import Roles


class EmployeeCreateView(GroupRequiredMixin, CreateView):
    group_required = Roles.admin

    form_class = UserCreationForm
    template_name = "employees/employee_create.html"

    def form_valid(self, form):
        # override default registration behaviour
        self.object = form.save()

        group = Group.objects.get(name=Roles.employee)
        self.object.groups.add(group)
        self.object.save()

        AppUser.objects.create(user_id=self.object.id)

        return HttpResponseRedirect(reverse_lazy('employees:detail', kwargs={'pk': self.object.id}))


class EmployeeListView(GroupRequiredMixin, ListView):
    group_required = Roles.admin

    model = User
    context_object_name = 'employee_list'
    template_name = "employees/employee_list.html"
    queryset = Group.objects.get(name=Roles.employee).user_set.all()


class EmployeeDetailView(GroupRequiredMixin, DetailView):
    group_required = Roles.admin

    context_object_name = 'employee'
    template_name = "employees/employee_detail.html"

    def get_queryset(self):
        current_user = get_object_or_404(User, pk=self.kwargs.get('pk'))

        if current_user.groups.filter(name=Roles.employee).exists():
            return User.objects.filter(pk=self.kwargs.get('pk'))
        else:
            return User.objects.none()


class EmployeeDeleteView(GroupRequiredMixin, RedirectView):
    group_required = Roles.admin

    model = User

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('employees:list')

    def get(self, request, *args, **kwargs):
        User.objects.get(pk=self.kwargs.get('pk')).delete()
        return super().get(request, *args, **kwargs)
