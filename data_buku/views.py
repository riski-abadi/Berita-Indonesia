from django.shortcuts import render

def index(request):
   template_name  = 'index.html'
   context = {
      'title':'ini adalah halaman index'
   }
   return render(request, template_name, context)

def about(request):
   template_name  = 'about.html'
   context = {
      'title':'ini adalah halaman about'
   }
   return render(request, template_name, context)

