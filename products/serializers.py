from rest_framework import serializers

from products.models import Product, ProductAmount


class ProductSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(allow_null=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'amount', 'photo', 'description']


class ProductAmountSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = ProductAmount
        fields = ['id', 'product', 'amount']
