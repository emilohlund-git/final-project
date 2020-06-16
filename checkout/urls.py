from django.conf.urls import url
from .views import checkout, payment_complete
from accounts import urls as urls_accounts

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'payment_complete/$', payment_complete, name="payment_complete")
]