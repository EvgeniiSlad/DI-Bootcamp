from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    def get_success_url(self) -> str:
        return reverse_lazy('add_film')
    
class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_category.html'
    fields = '__all__'
    def get_success_url(self) -> str:
        return reverse_lazy('add_film')

class UpdateCategoryView(UpdateView):
    model = Category
    template_name = 'update_category.html'
    fields = '__all__'
    def get_success_url(self) -> str:
        return reverse_lazy('add_film')



class FilmListView(LoginRequiredMixin,ListView):
    template_name = 'films.html'
    model = Film
    context_object_name = 'films'

class addFilm(LoginRequiredMixin,FormView):
    form_class = AddFilmForm
    template_name = 'addFilm.html'
    success_url = reverse_lazy('films')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
# class DirectorListView(ListView):
#     template_name = 'directors.html'
#     model = Director
#     context_object_name = 'directors'

def add_director(request):

    errors = {}

    if request.method == 'POST':
        form = AddDirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('directors')
        else:
            errors = form.errors

    form = AddDirectorForm()
    context = {'form': form, 'errors': errors}
    return render(request, 'addDirector.html', context)

class DirectorListView(ListView):
    model = Director
    template_name = 'directors.html'
    context_object_name = 'directors'







