from django.urls import path
from buku.views import *

urlpatterns = [
   path('', dashboard, name='dashboard'),
   path('list/', buku_list, name='buku_list'),
   path('add/', buku_add, name='buku_add'),
   path('update/<int:id>', buku_update, name='buku_update'),
   path('delete/<int:id>', buku_delete, name='buku_delete'),
]
