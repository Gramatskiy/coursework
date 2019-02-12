from django.urls import path, include

from products.views import ReceiptReceiveListCreateView, ReceiptSellListCreateView
from .routers import router

urlpatterns = [
    path('receipt/receive/', ReceiptReceiveListCreateView.as_view()),
    path('receipt/sell/', ReceiptSellListCreateView.as_view()),
    path('', include(router.urls)),
]
