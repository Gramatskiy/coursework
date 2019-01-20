from django.db.transaction import atomic
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from accounts import models
from rest_framework import viewsets, status
from rest_framework_jwt.views import ObtainJSONWebToken as BaseObtainJSONWebToken
from rest_framework import generics

from myapp.models import Product
from accounts.permissions import AllowAnyPostAuthenticatedPost
from myapp.serializers import *


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceProductViewSet(ModelViewSet):
    queryset = PlaceProduct.objects.all()
    serializer_class = PlaceProductSerializer


class MagnetKeyViewSet(ModelViewSet):
    queryset = MagnetKey.objects.all()
    serializer_class = MagnetKeySerializer


class DocumentOutViewSet(ModelViewSet):
    queryset = DocumentOut.objects.all()
    serializer_class = DocumentOutSerializer


class DocumentInViewSet(ModelViewSet):
    queryset = DocumentIn.objects.all()
    serializer_class = DocumentInSerializer
