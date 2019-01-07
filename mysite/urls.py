from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from django.views.generic import TemplateView

from accounts import views
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('myapp/', include('myapp.urls')),
    path('account/', include('accounts.urls')),
    #path('account/', TemplateView.as_view(template_name='index.html')),
    path('docs/', include_docs_urls(title='Couse API', permission_classes=[])),
]
