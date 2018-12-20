from django.contrib import admin

from accounts.models import User
from .models import Organization, Product, Place, DocumentIn, DocumentOut, MagnetKey, PlaceProduct
from .models import Employee, Provider, Customer


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    fields = ['name', 'status']


@admin.register(PlaceProduct)
class PlaceProductAdmin(admin.ModelAdmin):
    fields = ['place', 'product', 'status']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = ['organization', 'type', 'city', 'street', 'square']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price']


@admin.register(DocumentOut)
class DocumentOutAdmin(admin.ModelAdmin):
    fields = ['date', 'seller', 'customer', 'product', 'quantity', 'unit']


@admin.register(DocumentIn)
class DocumentInAdmin(admin.ModelAdmin):
    fields = ['date', 'acceptor', 'provider', 'product', 'quantity', 'unit']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ['user', 'photo']


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    fields = ['user']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ['user']


@admin.register(MagnetKey)
class ProviderAdmin(admin.ModelAdmin):
    fields = ['product', 'key']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'password', 'first_name', 'last_name', 'is_employee', 'is_provider',
              'is_customer', 'telephone']
    list_display = ('username', 'email', 'first_name', 'last_name')
