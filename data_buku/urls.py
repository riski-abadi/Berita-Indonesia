from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from data_buku.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about', about, name='about'),
    path('buku/', include('buku.urls')),
]
