from django.contrib import admin
from buku.models import *
# Register your models here.

admin.site.register(Category)

class BukuAdmin(admin.ModelAdmin):
   list_display = ['nama', 'deskripsi','jumlah']
admin.site.register(Buku, BukuAdmin)

class BeritaAdmin(admin.ModelAdmin):
   list_display = ['title', 'link','pubDate','description','thumbnail']
admin.site.register(Berita, BeritaAdmin)
