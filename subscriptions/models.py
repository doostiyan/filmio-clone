from django.db import models
from django.utils.translation import gettext_lazy as _

from Utils import validate_sku
from accounts.models import User


# Create your models here.


class Package(models.Model):
    title = models.CharField(max_length=50)
    sku = models.CharField(_('stock keeping unit'),max_length=50, validators=[validate_sku], db_index=True)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='packages/', blank=True)
    is_active = models.BooleanField(default=True)
    price = models.PositiveIntegerField()
    duration = models.DurationField(blank=True, null=True)
    # getaways = models.ManyToManyField('payment.Gateway')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Package')
        verbose_name_plural = _('Packages')
        ordering = ['title']
        db_table = 'packages'

    def __str__(self):
        return self.title


class Subscription(models.Model):
    user = models.ForeignKey(User, related_name='subscriptions', on_delete=models.CASCADE)
    package = models.ForeignKey(Package, related_name='packages', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expired = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')
        db_table = 'subscriptions'
