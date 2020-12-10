from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem, DeliveryAddress
from menu.models import MenuItems, Toppings
from django.http import JsonResponse
import json

@login_required(login_url='/login/')
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, order_status=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'title':'Cart','items':items, 'order':order}
    return render(request, 'order/cart.html', context)

@login_required(login_url='/login/')
def updateItem(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    action = data['action']

    if request.user.is_authenticated:
        customer = request.user.profile
        item = MenuItems.objects.get(id=product_id)
        order, created = Order.objects.get_or_create(customer=customer, order_status=False)
        order_item, created = OrderItem.objects.get_or_create(order=order, product=item)
    
    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)
    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    data = {
    'cart_item_total': order.get_cart_items,
    'order_quantity': order_item.quantity,
    'total': order.get_cart_total,
    'get_total': order_item.get_total,
    }
    return JsonResponse(data, safe=False)

@login_required(login_url='/login/')
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, order_status=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'title':'Checkout','items':items, 'order':order}
    return render(request, 'order/checkout.html', context)