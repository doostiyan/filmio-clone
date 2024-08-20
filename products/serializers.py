from rest_framework import serializers
from products.models import Category, File, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description', 'avatar')


class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ('id',  'title', 'file', 'file_type')

    def get_file_type(self, obj):
        return obj.get_file_type_display()


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    files = FileSerializer(many=True)
    # url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='id')
    # f = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'category', 'avatar', 'files',)

    # def get_f(self, obj):
    #     return obj.file.name