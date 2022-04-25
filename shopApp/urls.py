from django.urls import path, include
from django.contrib import admin
from .views import CategoryView, ProductView


app_name='shopApp'

urlpatterns = [
    # Category CRUD
    path('cate-list/', CategoryView.as_view({'get':'list'}), name='cate_list'),
    path('cate-create/', CategoryView.as_view({'post':'create'}), name='cate_create'),
    path('cate-update/<int:pk>/', CategoryView.as_view({'post':'update'}), name='cate_update'),
    path('cate-details/<int:pk>/', CategoryView.as_view({'get':'details'}), name='cate_details'),
    path('cate-delete/<int:pk>/', CategoryView.as_view({'post':'destroy'}), name='cate_delete'),

    # Product CRUD
    path('product-list/', ProductView.as_view({'get':'list'}), name='product_list'),
    path('product-create/', ProductView.as_view({'post':'create'}), name='product_create'),
    path('product-update/<int:pk>/', ProductView.as_view({'post':'update'}), name='product_update'),
    path('product-details/<int:pk>/', ProductView.as_view({'get':'details'}), name='product_details'),
    path('product-delete/<int:pk>/', ProductView.as_view({'post':'destroy'}), name='product_delete'),

]