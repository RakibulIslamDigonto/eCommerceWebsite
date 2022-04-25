from django.urls import path, include
from django.contrib import admin
from .views import OrderView



app_name='OrderApp'

urlpatterns = [
    # Category CRUD
    path('add/', OrderView.as_view({'post':'add_to_Card'}), name='add'),
    path('list/', OrderView.as_view({'get':'list'}), name='list'),


]