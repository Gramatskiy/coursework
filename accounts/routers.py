from rest_framework import routers

from .views import EmployeeViewSet

router = routers.DefaultRouter()
router.register('user/employee', EmployeeViewSet, base_name='employee')
