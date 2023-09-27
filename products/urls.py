from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView, CategoryListAPIView, CategoryDetailAPIView, FileListAPIView, FileDetailAPIView

urlpatterns = [
  path('products', ProductListAPIView.as_view(), name = 'product-list'),
  path('products/<int:pk>', ProductDetailAPIView.as_view(), name = 'product-detail'),

  path('categories', CategoryListAPIView.as_view(), name = 'category-list'),
  path('categories/<int:pk>', CategoryDetailAPIView.as_view(), name = 'category-detail'),
  
  path('products/<int:product_id>/files', FileListAPIView.as_view(), name = 'file-list'),
  path('products/<int:product_id>/files/<int:pk>', FileDetailAPIView.as_view(), name = 'file-detail'),
  
]