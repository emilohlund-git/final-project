from django.conf.urls import url, include
from .views import all_products
from products import views

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^products/delete/(?P<pk>[0-9]+)/$', views.product_delete, name='product_delete')
]