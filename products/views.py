from django.db.transaction import atomic
from rest_framework import status, mixins
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from products.models import Product, ReceiptReceive, ReceiptSell
from products.serializers import ProductSerializer, ProductAmountSerializer, ReceiptReceiveFullSerializer, \
    ReceiptReceiveCreateSerializer, ReceiptSellCreateSerializer, \
    ReceiptSellFullSerializer
from utils.heplers import get_object_or_None


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @atomic
    def create(self, request, *args, **kwargs):
        product_data = request.data
        product_amount_data = {'amount': product_data.get('amount', 1)}

        product_serializer = ProductSerializer(data=product_data)
        product_serializer.is_valid(raise_exception=True)

        product_amount_serializer = ProductAmountSerializer(data=product_amount_data)
        product_amount_serializer.is_valid(raise_exception=True)

        product_serializer.save()
        product_amount_serializer.save(product=product_serializer.instance)
        headers = self.get_success_headers(product_serializer.data)

        return Response(product_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @atomic
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        product_data = request.data
        amount = request.data.get('amount', None)
        if amount:
            product_amount_serializer = ProductAmountSerializer(data={'amount': amount})
            product_amount_serializer.is_valid(raise_exception=True)
            product_amount_serializer.save(product=instance)

        product_serializer = ProductSerializer(instance, data=product_data, partial=partial)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(product_serializer.data)


class ProductAmountViewSet(mixins.ListModelMixin,
                           GenericViewSet):
    serializer_class = ProductAmountSerializer

    def get_queryset(self):
        product = get_object_or_None(Product, pk=self.kwargs.get('product_pk'))
        return product and product.productamount_set.all()


class ReceiptReceiveListCreateView(ListCreateAPIView):
    queryset = ReceiptReceive.objects.all()
    serializer_class = ReceiptReceiveFullSerializer

    def get_serializer_class(self):
        if self.request.method in ["GET", "OPTION"]:
            return ReceiptReceiveFullSerializer
        return ReceiptReceiveCreateSerializer


class ReceiptSellListCreateView(ListCreateAPIView):
    queryset = ReceiptSell.objects.all()
    serializer_class = ReceiptSellFullSerializer

    def get_serializer_class(self):
        if self.request.method in ["GET", "OPTION"]:
            return ReceiptSellFullSerializer
        return ReceiptSellCreateSerializer
