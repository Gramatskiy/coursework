from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from accounts import views
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('account/', include('accounts.urls')),
    path('docs/', include_docs_urls(title='Couse API', permission_classes=[])),
    # path(r'', include('myapp.urls')),
]
