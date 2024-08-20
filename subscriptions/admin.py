from django.contrib import admin

from subscriptions.models import Subscription, Package


# Register your models here.

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'package', 'created', 'expired')


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'sku', 'is_enable', 'price', 'duration')