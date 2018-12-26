from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('product', ProductViewSet, base_name='product')
router.register('organization', OrganizationViewSet, base_name='organization')
router.register('place', PlaceViewSet, base_name='place')
router.register('placeProduct', PlaceProductViewSet, base_name='placeProduct')
router.register('magnetKey', MagnetKeyViewSet, base_name='magnetKey')
router.register('documentOut', DocumentOutViewSet, base_name='documentOut')
router.register('documentIn', DocumentInViewSet, base_name='documentIn')
