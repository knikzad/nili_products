from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product, File
from .serializers import CategorySerializer, ProductSerializer, FileSerializer


class ProductListAPIView(APIView):

  def get(self, request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True, context={'request': request})
    return Response(serializer.data)

class ProductDetailAPIView(APIView):
  def get(self, request, pk):
    try:
      product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
      return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product, context = {'request': request})
    return Response(serializer.data)

class CategoryListAPIView(APIView):

  def get(self, request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many = True, context = {'request': request})
    return Response(serializer.data)


class CategoryDetailAPIView(APIView):

  def get(self, request, pk):
    try:
      category = Category.objects.get(pk = pk)
    except Category.DoesNotExist:
      return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category, context = {'request': request})
    return Response(serializer.data)


class FileListAPIView(APIView):

  def get(self, request, product_id):
    files = File.objects.filter(product_id = product_id)
    serializer = FileSerializer(files, many = True, context = {'request': request})
    return Response(serializer.data)


class FileDetailAPIView(APIView):

  def get(self, request, product_id, pk):
    try:
      file = File.objects.get(product_id = product_id, pk = pk)
    except File.DoesNotExist:
      return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = FileSerializer(file, context = {'request': request})
    return Response(serializer.data)

