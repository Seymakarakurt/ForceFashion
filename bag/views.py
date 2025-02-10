from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product
from .models import Bag

def view_bag(request):
    """rendert Warenkorb"""
    return render(request, 'bag.html')


def add_to_bag(request, item_id):
    """Produkte dem Warenkorb hinzufügen"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    if request.user.is_authenticated:
        bag_obj = Bag()
        bag_obj.user = request.user
        bag_obj.item = product
        bag_obj.quantity = quantity
        bag_obj.save()
        bag = request.session.get('bag', {})

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag! ')

            request.session['bag'] = bag

    else:
        bag = request.session.get('bag', {})
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag! ')
            request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_to_bag(request, item_id):
    """Wenn im Warenkorb was geändert wurde, wird Gegenstand hinzugefügt"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag! ')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
