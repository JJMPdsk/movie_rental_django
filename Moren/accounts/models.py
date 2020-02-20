from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    CUSTOMER = 1
    EMPLOYEE = 2
    ADMIN = 3

    ROLE_CHOICES = (
        (CUSTOMER, 'customer'),
        (EMPLOYEE, 'employee'),
        (ADMIN, 'admin'),
    )

    id = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return self.user.username
