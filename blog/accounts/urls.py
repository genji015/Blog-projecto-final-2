from django.urls import path
from .views import RegistroView, CustomLoginView, CustomLogoutView, PasswordChange

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
]
