from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.shortcuts import get_object_or_404, redirect, render, reverse
from .models import Product
from accounts.forms import UserLoginForm

# Create your views here.


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"login_form": UserLoginForm, "products": products})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Get current product

    if request.method == "POST":
        request.session['cart'] = {}
        product.delete()
        return redirect('profile')

    return render(request, 'profile.html', {'product': product})
