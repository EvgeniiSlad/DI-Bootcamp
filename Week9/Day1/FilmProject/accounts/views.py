from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from .forms import *
from django.views.generic import FormView, DetailView
# Create your views here.

class ProfileCreateView(FormView):

    template_name = 'profile_create.html'
    form_class = ProfileForm

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user.id

    def get_success_url(self) -> str:
        return reverse_lazy('profile',args=[self.request.user.profile.id])
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileView(DetailView):

    template_name = 'profile.html'
    model = Profile
    context_object_name = 'profile'



class IMDBLoginView(LoginView):
    template_name = 'login.html'    

class IMDBLogoutView(LogoutView):
    template_name = 'logout.html' 


class RegisterView(FormView):

    template_name = 'register.html'
    form_class = RegistrationForm

    def get_success_url(self) -> str:
        return reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)