from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)
    telephone = models.IntegerField(null=True, blank=True)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    photo = models.ImageField()

    def save(self, *args, **kwargs):
        if getattr(self, 'user', False):
            self.user.is_employee = True
            self.user.save()
        super(Employee, self).save(*args, **kwargs)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')

    def save(self, *args, **kwargs):
        if getattr(self, 'user', False):
            self.user.is_customer = True
            self.user.save()
        super(Customer, self).save(*args, **kwargs)


class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='provider')

    def save(self, *args, **kwargs):
        if getattr(self, 'user', False):
            self.user.is_provider = True
            self.user.save()
        super(Provider, self).save(*args, **kwargs)
