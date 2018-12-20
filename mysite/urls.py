from django.conf.urls import include, url
from django.contrib import admin
from accounts import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'admin/', admin.site.urls),
    #url(r'', include('accounts.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #url(r'', include('myapp.urls')),
]
