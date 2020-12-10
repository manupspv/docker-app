from django.shortcuts import render
from .models import MenuItems, Toppings
from django.http import JsonResponse
import json


def menu(request):
    item_list = [MenuItems.objects.filter(item_type="Pinocchio Special").filter(item_size="Small"),
    MenuItems.objects.filter(item_type="Regular Pizza").filter(item_size="Small"),
    MenuItems.objects.filter(item_type="Sicilian Pizza").filter(item_size="Small"),
    MenuItems.objects.filter(item_type="Subs").filter(item_size="Small"),
    MenuItems.objects.filter(item_type="Pasta"),
    MenuItems.objects.filter(item_type="Salads"),
    MenuItems.objects.filter(item_type="Dinner Platters").filter(item_size="Small")
    ]

    customize = ['Pinocchio Special','Pasta','Salads','Dinner Platters']

    context = {
    "title": "Menu",
    'item_list': item_list,
    'customize': customize,
    'toppings': Toppings.objects.all()

    }
    return render(request, "menu/menu.html", context)

def itemPrice(request):

    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        item_name = received_json_data['item_name']
        item_size = received_json_data['item_size']
        item_type = received_json_data['item_type']
        pizza = MenuItems.objects.filter(item_type=item_type).filter(item_name=item_name).filter(item_size=item_size)

        data = {
                'price' : list(pizza.values())[0]['item_price'],
                'id' : list(pizza.values())[0]['id']
        }
    return JsonResponse(data, safe=False)