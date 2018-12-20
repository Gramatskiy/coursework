from accounts.models import User, Employee
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name',
                  'is_employee', 'is_customer', 'is_provider',
                  'password', 'last_login')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_employee': {'read_only': True},
            'is_customer': {'read_only': True},
            'is_provider': {'read_only': True},
        }

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ('id', 'user', 'photo')


class EmployeeCreateSerializer(EmployeeSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, allow_null=True)

    class Meta(EmployeeSerializer.Meta):
        pass
