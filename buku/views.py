from django.shortcuts import redirect, render

from buku.models import *


def buku_list(request):
   template_name  = 'buku_list.html'
   buku_list = Buku.objects.all()
   context = {
      'title':'ini adalah halaman buku',
      'buku':buku_list
   }
   return render(request, template_name, context)


def buku_add(request):
   template_name  = 'buku_tambah.html'
   category = Category.objects.all()
   if request.method == "POST":
      
      input_category = request.POST.get('category')
      input_nama = request.POST.get('nama')
      input_deskripsi = request.POST.get('deskripsi')
      input_jumlah = request.POST.get('jumlah')
      
      # panggil kategori dulu
      get_category = Category.objects.get(nama=input_category)
      
      # simpan produk karena ada relasi ke tabel kategori
      Buku.objects.create(
         nama = input_nama,
         deskripsi = input_deskripsi,
         jumlah = input_jumlah,
         category = get_category,
      )
      return redirect(buku_list)

   context = {
      'title':'ini adalah halaman tambah barang',
      'category': category
   }
   return render(request, template_name, context)


def buku_update(request, id):
   template_name  = 'buku_tambah.html'
   category = Category.objects.all()
   get_buku = Buku.objects.get(id=id)
   if request.method == "POST":
      
      input_category = request.POST.get('category')
      input_nama = request.POST.get('nama')
      input_deskripsi = request.POST.get('deskripsi')
      input_jumlah = request.POST.get('jumlah')
      
      # panggil kategori dulu
      get_category = Category.objects.get(nama=input_category)
      
      # panggil kategori dulu
      get_buku.nama = input_nama
      get_buku.deskripsi = input_deskripsi
      get_buku.jumlah = input_jumlah
      get_buku.category = get_category
      get_buku.save()
      
      return redirect(buku_list)
   context = {
      'title':'ini adalah halaman tambah buku',
      'category': category,
      'get_buku':get_buku,
      
   }
   return render(request, template_name, context)

def buku_delete(request, id):
   Buku.objects.get(id=id).delete()
   return redirect(buku_list)