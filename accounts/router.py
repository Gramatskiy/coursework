from rest_framework import routers

from .views import EmployeeViewSet, ProviderViewSet, CustomerViewSet

router = routers.DefaultRouter()
router.register('user/employee', EmployeeViewSet, base_name='employee')
router.register('user/provider', ProviderViewSet, base_name='provider')
router.register('user/customer', CustomerViewSet, base_name='customer')
