from django.db import models
from django.utils.translation import gettext_lazy as _

from Utils import validate_phone_number
from accounts.models import User
from subscriptions.models import Package


# Create your models here.


class Gateway(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="getaways/")
    is_enabled = models.BooleanField(default=True)
    # credentials = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Gateway'
        verbose_name_plural = 'Gateways'
        db_table = 'gateways'


class Payment(models.Model):
    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_ERROR = 20
    STATUS_CANCELED= 30
    STATUS_REFUNDED = 31
    STATUS_CHOICES = (
        (STATUS_VOID, 'Void'),
        (STATUS_PAID, 'Paid'),
        (STATUS_ERROR, 'Error'),
        (STATUS_CANCELED, 'Canceled'),
        (STATUS_REFUNDED, 'Refunded'),
    )

    STATUS_TRANSLATIONS = {
        STATUS_VOID: _('Payment could not be processed'),
        STATUS_PAID: _('Payment successful'),
        STATUS_ERROR: _('Payment has encountered an error. Our technical team will check the problem shortly'),
        STATUS_CANCELED: _('Payment canceled by user.'),
        STATUS_REFUNDED: _('This payment has been refunded'),
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='payments')
    gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE, related_name='gateways')
    price = models.PositiveIntegerField(default=0)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=STATUS_VOID, db_index=True)
    device_uuid = models.CharField(max_length=36, blank=True)
    token = models.CharField(max_length=50)
    phone_number = models.BigIntegerField(validators=[validate_phone_number], db_index=True)
    consumed_code = models.PositiveIntegerField(_('consumed reference code'), null=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        db_table = 'payments'

