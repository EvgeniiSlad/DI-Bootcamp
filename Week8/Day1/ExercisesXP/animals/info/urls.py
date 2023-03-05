from django.urls import path
from .views import show_animal, show_family, show_animals,all_family

urlpatterns = [
    path('family/<int:id>', show_family),
    path('animal/<int:id>', show_animal),
    path('animals/<int:id>', show_animals),
    path('all_family<int:id>',all_family)
]