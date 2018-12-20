from django.db.transaction import atomic
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from accounts import models
from rest_framework import viewsets, status
from rest_framework_jwt.views import ObtainJSONWebToken as BaseObtainJSONWebToken

from accounts.models import User
from accounts.serializers import UserSerializer, EmployeeCreateSerializer, EmployeeSerializer


class ObtainJSONWebToken(BaseObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super(ObtainJSONWebToken, self).post(request, *args, **kwargs)
        if response.status_code == 200:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = serializer.object.get('user') or request.user
                if user.is_employee:
                    response.data['is_employee'] = True
                elif user.is_customer:
                    response.data['is_customer'] = True
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
            elif user.is_customer:
                # TODO return CustomerSerializer
                pass
            elif user.is_provider:
                # TODO return ProviderSerializer
                pass
        raise Exception('Incorrect user from request')

    def get_object(self):
        self.kwargs['pk'] = self.request.user.pk
        obj = super(SelfUserDetailView, self).get_object()
        if obj.is_device:
            return obj.device
        elif obj.is_person:
            person = obj.person
            if person.is_customer:
                return person.customer
            elif person.is_client:
                client = person.client
                if client.is_premium:
                    return client.premium
                return client
        raise Exception('Incorrect user from request')


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer


class UserCreateMixin:
    @staticmethod
    def create(request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        return user_serializer.save()


class EmployeeViewSet(UserCreateMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
                      GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = EmployeeSerializer
    queryset = models.Employee.objects.all()

    @atomic
    def create(self, request, *args, **kwargs):
        user = super().create(request)
        employee_serializer = EmployeeCreateSerializer(data=request.data)
        employee_serializer.is_valid(raise_exception=True)
        employee_serializer.save(user=user)
        return Response(data=employee_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        super(EmployeeViewSet, self).update()

    def check_object_permissions(self, request, obj):
        return request.user.is_employee and request.user.employee == obj
