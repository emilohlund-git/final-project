from django.shortcuts import render
from products.models import Product
from accounts.forms import UserLoginForm

# Create your views here.
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"login_form": UserLoginForm, "products": products})