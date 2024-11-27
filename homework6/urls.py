from django.contrib import admin
from django.urls import path
from app.views import create_icecream, create_icecreamshop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create_icecreamshop),
    path('create_icecream/', create_icecream)
]
