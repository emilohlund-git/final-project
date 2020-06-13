from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, add_item
from accounts import urls_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^add_item/', add_item, name="add_item"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(urls_reset))
]