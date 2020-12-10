from django.urls import path
from . import views

urlpatterns = [
    path('order/cart/', views.cart, name="order-cart"),
    path('update_item/', views.updateItem, name="order-update_item"),
    path('order/checkout/', views.checkout, name="order-checkout"),
]