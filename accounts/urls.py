from django.conf.urls import url, include
from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token

from accounts.router import *
from accounts.views import *

urlpatterns = [

    # path('employees/', EmployeeList.as_view()),
    path('users/', UserList.as_view()),
    path('login/', ObtainJSONWebToken.as_view()),
    path('token-refresh/', refresh_jwt_token),
    path('user/self/', SelfUserDetailView.as_view()),
    path('', include(router.urls)),
]
