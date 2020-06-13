from django.shortcuts import render, redirect, HttpResponseRedirect
from accounts.forms import UserLoginForm, UserRegistrationForm
# Create your views here.


def index(request):
    """Return the index.html file"""
    login_form = {"login_form": UserLoginForm}
    return render(request,  'index.html', login_form)
