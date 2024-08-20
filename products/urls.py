from django.urls import path
from products import views
app_name = 'products'
urlpatterns  = [
    path('product/', views.ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('category/', views.CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('file/<int:product_id>/', views.FileListView.as_view(), name='file-list'),
    path('file/<int:product_id>/<int:pk>/', views.FileDetailView.as_view(), name='file-detail'),
]