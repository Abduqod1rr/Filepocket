from django.shortcuts import render ,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView ,UpdateView ,DeleteView , ListView
from django.contrib.auth.views import LoginView , LogoutView 
from .forms import UserRegisterForm
from django.contrib.auth.models import User 


def home(request):
    return HttpResponse('hello world')

class registerview(CreateView):
    template_name='register.html'
    model=User
    form_class=UserRegisterForm
    success_url=reverse_lazy('login')

class userlogin(LoginView):
    template_name='login.html'
    fields=['username','password']
    success_url=reverse_lazy('homee')