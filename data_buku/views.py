from django.shortcuts import render

def index(request):
   template_name  = 'front/index.html'
   context = {
      'title':'ini adalah halaman utama'
   }
   return render(request, template_name, context)

def about(request):
   template_name  = 'front/about.html'
   context = {
      'title':'ini adalah halaman about'
   }
   return render(request, template_name, context)

def buku(request):
   template_name  = 'front/buku_list.html'
   context = {
      'title':'ini adalah halaman buku'
   }
   return render(request, template_name, context)


