from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nos_cours/', views.page_des_cours, name='page_cours'),
    path('inscription/', views.inscription, name='inscription'),
    path('cours/<int:cours_id>/', views.detail_cours, name='detail_cours'),
    path('lecon/<int:lecon_id>/', views.afficher_lecon, name='afficher_lecon'),
    path('module/<int:module_id>/evaluation/', views.faire_evaluation, name='faire_evaluation'),
    path('mon_profil/', views.voir_profil, name='mon_profil'),
]