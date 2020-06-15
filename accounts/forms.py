from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from products.models import Product


class UserLoginForm(forms.Form):
    """Form to be used to log users in"""

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control bg-transparent', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control bg-transparent', 'placeholder': 'Password'}))


class AddItemForm(forms.Form):
    """Form to be used for adding items"""

    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control bg-transparent', 'placeholder': 'Name'}))
    price = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control bg-transparent', 'placeholder': 'Price'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control bg-transparent', 'placeholder': 'Description', 'rows': 3, 'cols': 15}))
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control bg-transparent', 'placeholder': 'Description'}))


class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control bg-transparent'}))
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput(attrs={'class': 'form-control bg-transparent'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control bg-transparent'}),
            'username': forms.TextInput(attrs={'class': 'form-control bg-transparent'})
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")

        if password1 != password2:
            raise ValidationError("Passwords must match")

        return password2
