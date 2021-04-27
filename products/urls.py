from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.all_products, name='products'),
    path('<pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product_category/', views.Product_category, name='categories'),
]
