from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('product', ProductViewSet, base_name='product')
