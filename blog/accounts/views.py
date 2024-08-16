from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistroForm

class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'accounts/registro.html'
    success_url = reverse_lazy('index')

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')
    
# Create your views here.
