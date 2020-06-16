from django.conf.urls import url, include
from accounts.views import logout, login, register, user_profile, add_item
from accounts import urls_reset
from .views import send_mail

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^add_item/', add_item, name="add_item"),
    url(r'^login/', login, name="login"),
    url(r'^register/', register, name="register"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^reset-password/', include(urls_reset)),
]