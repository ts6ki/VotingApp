from django.urls import path

from general.views import contact_us, about_us, about_us_detailed

urlpatterns = [
    path("contact_us", contact_us),
    path("about_us", about_us),
    path("about_us/<str:username>", about_us_detailed),
]
