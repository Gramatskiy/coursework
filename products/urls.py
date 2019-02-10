from django.urls import path, include

from products.views import ReceiptReceiveCreateView, ReceiptSellCreateView
from .routers import router

urlpatterns = [
    path('receipt/receive/', ReceiptReceiveCreateView),
    path('receipt/sell/', ReceiptSellCreateView),
    path('', include(router.urls)),
]
