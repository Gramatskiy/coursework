from django.conf.urls import url, include
from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token

from accounts.routers import router
from accounts.views import ObtainJSONWebToken, SelfUserDetailView

urlpatterns = [
    # path('login/', ObtainJSONWebToken.as_view()),
    # path('token-refresh/', refresh_jwt_token),
    # path('user/self/', SelfUserDetailView.as_view()),
    # path('', include(router.urls)),
]
