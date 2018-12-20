from django.contrib import admin
from django.urls import path, include

from accounts import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path(r'admin/', admin.site.urls),
    # path(r'', include('accounts.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path(r'', include('myapp.urls')),
]
