from django.db import models


# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='scategory')
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='categories/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products', blank=True,  )
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='categories/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 2
    FILE_TYPE = (
        (FILE_AUDIO, 'Audio'),
        (FILE_VIDEO, 'Video'),
        (FILE_PDF, 'PDF'),
    )

    product = models.ForeignKey(Product, related_name='files', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    file_type = models.PositiveSmallIntegerField(choices=FILE_TYPE, default=FILE_VIDEO)
    file = models.ImageField(upload_to='files/%Y/%m/%d', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title