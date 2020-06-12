from django.conf.urls import url, include
from django.urls import path
from . import urls_reset
from .views import index, register, profile, logout, login

urlpatterns = [
    path('register/', register, name="register"),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
]