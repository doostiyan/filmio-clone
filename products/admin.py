from django.contrib import admin

from products.models import Product, Category, File


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('parent', 'title', 'is_active', 'created')
    list_filter = ('is_active', 'parent')
    search_fields = ('title',)


class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ('title', 'file', 'is_active')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created')
    list_filter = ('is_active',)
    search_fields = ('title',)
    filter_horizontal = ('category',)
    inlines = (FileInlineAdmin,)
