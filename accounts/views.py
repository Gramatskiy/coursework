from accounts import models
from rest_framework import viewsets
from accounts.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer


