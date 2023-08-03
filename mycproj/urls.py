from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pools/', include("pools.urls")),
    path('', include("general.urls"))
]
