from django.conf.urls import url
from .views import checkout
from accounts import urls as urls_accounts

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
]