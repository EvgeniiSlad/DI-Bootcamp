from django.contrib import admin
from django.urls import path
from films.views import *
from accounts.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('addFilm/',addFilm.as_view(),name='addfilm'),
    path('films/',FilmListView.as_view(),name='films'),
    path('addDirector/',add_director,name='adddirector'),
    path('directors/',DirectorListView.as_view(),name='directors'),
    path('add_category/',AddCategoryView.as_view()),
    path('login/',IMDBLoginView.as_view(),name='login'),
    path('logout/',IMDBLogoutView.as_view(),name='logout')
]
