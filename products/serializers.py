from rest_framework import serializers

from products.models import Product, ProductAmount, ReceiptReceive, ReceiptSell


class ProductAmountShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAmount
        fields = ['amount', 'timestamp']


class ProductSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    amount = ProductAmountShortSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'amount', 'photo', 'description']


class ProductAmountSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), required=False)

    class Meta:
        model = ProductAmount
        fields = ['id', 'product', 'amount', 'timestamp']


class ReceiptReceiveCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptReceive
        fields = ['id', 'product']
        depth = 0


class ReceiptReceiveFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptReceive
        fields = ['id', 'product', 'timestamp']
        depth = 1


class ReceiptSellCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptSell
        fields = ['id', 'product']
        depth = 0


class ReceiptSellFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptSell
        fields = ['id', 'product', 'timestamp']
        depth = 1
