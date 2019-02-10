from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)
    telephone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.last_name + " " + self.first_name)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')

    def save(self, *args, **kwargs):
        if getattr(self, 'user', False):
            self.user.is_employee = True
            self.user.save()
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)


class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='provider')

    def save(self, *args, **kwargs):
        if getattr(self, 'user', False):
            self.user.is_provider = True
            self.user.save()
        super(Provider, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)
