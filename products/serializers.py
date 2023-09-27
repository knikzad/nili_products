from rest_framework import serializers
from .models import Product, Category, File


class CategorySerializer(serializers.ModelSerializer):
    # categories = CategorySerializer(many = True)
    class Meta:
        model = Category
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer(many = True)
    class Meta:
        model = File
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many = True)
    files = FileSerializer(many = True)
    class Meta:
        model = Product
        fields = '__all__'