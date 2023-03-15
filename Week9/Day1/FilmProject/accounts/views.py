from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.

class IMDBLoginView(LoginView):
    template_name = 'login.html'    

class IMDBLogoutView(LogoutView):
    template_name = 'logout.html' 