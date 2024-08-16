from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from accounts.forms import RegistroForm, ChangeForm

class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'accounts/registro.html'
    success_url = reverse_lazy('index')

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')
    
class PasswordChange(PasswordChangeView):
    form_class = ChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'accounts/password_change.html'
    
# Create your views here.
