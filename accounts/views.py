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

from accounts.models import User, Employee, Provider
from accounts.permissions import AllowAnyPostAuthenticatedPost
from accounts.serializers import *


class ObtainJSONWebToken(BaseObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super(ObtainJSONWebToken, self).post(request, *args, **kwargs)
        if response.status_code == 200:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = serializer.object.get('user') or request.user
                if user.is_superuser:
                    response.data['is_admin'] = True
                if user.is_employee:
                    response.data['is_employee'] = True
                elif user.is_provider:
                    response.data['is_provider'] = True
        return response


class SelfUserDetailView(RetrieveAPIView):
    """

    get:
    Retrieve user
    """
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request:
            user = self.request.user
            if user.is_employee:
                return EmployeeSerializer
            elif user.is_provider:
                return ProviderSerializer
        raise RuntimeError('Incorrect user from request')

    def get_object(self):
        self.kwargs['pk'] = self.request.user.pk
        obj = super(SelfUserDetailView, self).get_object()
        if obj.is_employee:
            return obj.employee
        if obj.is_provider:
            return obj.provider
        raise RuntimeError('Incorrect user from request')


class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer


class UserCreateMixin:
    @staticmethod
    def create(request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        return user_serializer.save()


class EmployeeViewSet(UserCreateMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
                      GenericViewSet, ListModelMixin):
    permission_classes = [AllowAnyPostAuthenticatedPost]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    @atomic
    def create(self, request, *args, **kwargs):
        user = super().create(request)
        employee_serializer = EmployeeCreateSerializer(data=request.data)
        employee_serializer.is_valid(raise_exception=True)
        employee_serializer.save(user=user)
        return Response(data=employee_serializer.data, status=status.HTTP_201_CREATED)

    def check_object_permissions(self, request, obj):
        return request.user.is_employee and request.user.employee == obj


class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ProviderViewSet(UserCreateMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
                      GenericViewSet, ListModelMixin):
    permission_classes = [AllowAnyPostAuthenticatedPost]
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()

    @atomic
    def create(self, request, *args, **kwargs):
        user = super().create(request)
        provider_serializer = ProviderCreateSerializer(data=request.data)
        provider_serializer.is_valid(raise_exception=True)
        provider_serializer.save(user=user)
        return Response(data=provider_serializer.data, status=status.HTTP_201_CREATED)

    def check_object_permissions(self, request, obj):
        return request.user.is_provider and request.user.provider == obj


class ProviderList(generics.ListAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
