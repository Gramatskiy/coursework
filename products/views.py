from django.db.transaction import atomic
from rest_framework import status, mixins
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from products.models import Product
from products.serializers import ProductSerializer, ProductAmountSerializer
from utils.heplers import get_object_or_None


class ProductViewSet(ModelViewSet):

    @atomic
    def create(self, request, *args, **kwargs):
        product_data = request.data
        product_amount_data = product_data.pop('amount', 1)

        product_serializer = ProductSerializer(product_data)
        product_serializer.is_valid(raise_exception=True)

        product_amount_serializer = ProductAmountSerializer(product_amount_data)
        product_amount_serializer.is_valid(raise_exception=True)

        product_serializer.save()
        product_amount_serializer.save(product=product_serializer.data['id'])
        headers = self.get_success_headers(product_serializer.data)

        return Response(product_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @atomic
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        product_data = request.data
        product_amount_data = product_data.pop('amount', instance.amount.amount)

        product_serializer = ProductSerializer(instance, product_data, partial=partial)
        product_serializer.is_valid(raise_exception=True)

        product_amount_serializer = ProductAmountSerializer(instance, product_amount_data, partial=partial)
        product_amount_serializer.is_valid(raise_exception=True)

        product_serializer.save()
        product_amount_serializer.save(product=product_serializer.data['id'])

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(product_serializer.data)


class ProductAmountViewSet(mixins.ListModelMixin,
                           GenericViewSet):
    def get_queryset(self):
        product = get_object_or_None(Product, pk=self.kwargs.get('product_pk'))
        return product and product.amount_set.all()


class ReceiptReceiveCreateView(ListCreateAPIView):
    pass


class ReceiptSellCreateView(ListCreateAPIView):
    pass
