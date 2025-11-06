from django.shortcuts import render ,HttpResponse,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView ,UpdateView ,DeleteView , ListView
from django.contrib.auth.views import LoginView , LogoutView 
from .forms import UserRegisterForm
from django.contrib.auth.models import User 
from .models import Files
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginRequiredMixin,ListView):
    model = Files
    template_name='home.html'
    context_object_name='files'

    def get_queryset(self):
        
        return Files.objects.filter(user=self.request.user)
    

class registerview(CreateView):
    template_name='register.html'
    model=User
    form_class=UserRegisterForm
    success_url=reverse_lazy('login')

class userlogin(LoginView):
    template_name='login.html'
    fields=['username','password']
    success_url=reverse_lazy('homee')