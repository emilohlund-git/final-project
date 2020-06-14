from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse

# Create your views here.
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = id
    else:
        cart[id] = cart.get(id) 

    request.session['cart'] = cart
    return redirect(reverse('products'))

def remove_from_cart(request, id):
    """Remove an item from the cart"""
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('checkout'))