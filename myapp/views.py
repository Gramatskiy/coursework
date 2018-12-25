from django.db.transaction import atomic
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from accounts import models
from rest_framework import viewsets, status
from rest_framework_jwt.views import ObtainJSONWebToken as BaseObtainJSONWebToken
from rest_framework import generics

from myapp.models import Product
from accounts.permissions import AllowAnyPostAuthenticatedPost
from myapp.serializers import *


class ProductViewSet(GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
