from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm, AddItemForm
from products.models import Product
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """Return the index.html file"""
    return render(request,  'index.html')


def add_item(request):
    add_item_form = AddItemForm()
    return render(request, 'add_item.html', {'add_item_form': add_item_form})


@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(
                    None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    return render(request, 'profile.html')


def add_item(request):
    """Adds an item to the DB"""
    if request.method == "POST":
        user = request.user.username
        add_item_form = AddItemForm(request.POST, request.FILES)
        if add_item_form.is_valid():
            product_name = request.POST['name']
            product_description = request.POST['description']
            product_price = request.POST['price']
            product_image = request.FILES['image']
            new_item = Product(
                name=product_name,
                description=product_description,
                price=product_price,
                image=product_image,
                username=user
            )
            new_item.save()

            return redirect('products')
    else:
        add_item_form = AddItemForm()
    return render(request, 'add_item.html', {
        'add_item_form': add_item_form
    })


def register(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(
                    request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})


def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})
