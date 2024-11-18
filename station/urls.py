from django.urls import path
from . import views

urlpatterns = [
    path('', views.vue_ensemble, name='vue_ensemble'),
    path('lieu/<int:lieu_id>/', views.details_lieu, name='details_lieu'),
    path('vaisseau/', views.vue_ensemble, name='vue_ensemble'),
    path('personnages/', views.liste_personnages, name='liste_personnages'),
    path('personnage/<int:personnage_id>/', views.details_personnage, name='details_personnage'),
]