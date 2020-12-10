from .models import Order, OrderItem

def cart_total(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, order_status=False)
        cart_total = order.get_cart_items
    else:
        cart_total = 0

    
    return {'cart_total': cart_total}
            