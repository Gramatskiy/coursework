from myapp.models import Product, Organization, Place, PlaceProduct, MagnetKey, DocumentOut, DocumentIn
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name', 'status')


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'organization', 'type', 'city', 'street', 'square')


class PlaceProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceProduct
        fields = ('id', 'place', 'product', 'status')


class MagnetKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = MagnetKey
        fields = ('id', 'product', 'key')


class DocumentOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentOut
        fields = ('id', 'date', 'seller', 'customer', 'product', 'quantity', 'unit')


class DocumentInSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentIn
        fields = ('id', 'date', 'acceptor', 'provider', 'product', 'quantity', 'unit')
