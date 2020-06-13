from django import forms
from .models import Order


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cvv = forms.CharField(label='Security code (CVV)', required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '000', 'max': '999', 'maxlength': '3', 'oninput': 'maxLengthCheck(this)'}))
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'MM', 'min': '1', 'max': '12', 'maxlength': '2', 'oninput': 'maxLengthCheck(this)'}))
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'YY', 'min': '00', 'max': '99', 'maxlength': '2', 'oninput': 'maxLengthCheck(this)'}))
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2',
            'county'
        )