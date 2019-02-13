from rest_framework import routers

from .views import EmployeeViewSet, ProviderViewSet

router = routers.DefaultRouter()
router.register('user/employee', EmployeeViewSet, base_name='employee')
router.register('user/providers', ProviderViewSet, base_name='providers')
