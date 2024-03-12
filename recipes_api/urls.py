from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('', include('recipes.urls')),
    path('authors/', include('authors.urls'))
]
