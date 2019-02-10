from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    name = models.CharField(_('name'))
    photo = models.ImageField(_('photo'), upload_to='product', blank=True)
    description = models.TextField(_('description'))

    @property
    def amount(self):
        return self.productamount_set.exists() and self.productamount_set.last()


class ProductAmount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'))
    amount = models.PositiveSmallIntegerField(_('amount'))
    timestamp = models.DateTimeField(_('timestamp'), auto_now_add=True)

    class Meta:
        ordering = ['timestamp']


class ReceiptReceive(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'))

    def save(self, *args, **kwargs):
        if getattr(self, 'product', None):
            ProductAmount.objects.create(amount=self.product.amount + 1, product=self.product)


class ReceiptSell(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'))

    def save(self, *args, **kwargs):
        if getattr(self, 'product', None):
            ProductAmount.objects.create(amount=self.product.amount - 1, product=self.product)
