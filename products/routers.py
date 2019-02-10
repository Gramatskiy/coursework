from rest_framework import routers

from .views import ProductViewSet, ProductAmountViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet, base_name='product')
router.register('product/(?P<product_pk>\d+)/amount', ProductAmountViewSet, base_name='product-amount')
