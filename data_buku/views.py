from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from buku.models import Buku

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

def berita(request):
   template_name  = 'front/berita.html'
   buku = Buku.objects.all()
   context = {
      'title':'ini adalah halaman berita',
      'buku':buku,
   }
   return render(request, template_name, context)
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    template_name = 'account/login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            pass
            print("username benar" )
            auth_login(request, user)
            return redirect('index')
        else:
            pass
            print("username salah" )
    context = {
        'title':'form',
    }
    return render(request, template_name, context)
def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    template_name = 'account/register.html'
    context = {
        'title':'form',
    }
    return render(request, template_name, context)
