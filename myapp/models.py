from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from accounts.models import Employee, Provider, Customer


class Organization(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField()

    def __str__(self):
        return self.name


class Place(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    square = models.IntegerField()

    def __str__(self):
        return self.type + " " + self.street


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name


class DocumentIn(models.Model):
    date = models.DateTimeField(default=timezone.now)
    acceptor = models.ForeignKey(Employee, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit = models.IntegerField()

    def __str__(self):
        return str(self.date) + " " + str(self.provider.user) + " " + str(self.acceptor.user)


class DocumentOut(models.Model):
    date = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit = models.IntegerField()

    def __str__(self):
        return str(self.date) + " " + str(self.customer.user) + " " + str(self.seller.user)


class MagnetKey(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    key = models.IntegerField()

    def __str__(self):
        return self.product.name


class PlaceProduct(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=30)

    def __str__(self):
        return str(self.place.organization.name + " " + self.product.name)
