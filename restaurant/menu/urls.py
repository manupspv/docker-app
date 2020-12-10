from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name="menu"),
    path('menu/item_price/', views.itemPrice, name="menu-item_price"),
]