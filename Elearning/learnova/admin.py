from django.contrib import admin
from .models import Profil, Cours, Module, Lecon, Inscription, Progression, Evaluation

# Permet d'ajouter des leçons directement dans la page d'un Module
class LeconInline(admin.TabularInline):
    model = Lecon
    extra = 1 # Affiche une ligne vide pour ajouter une leçon rapidement

# Permet d'ajouter des modules directement dans la page d'un Cours
class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation') # Colonnes affichées dans la liste
    search_fields = ('titre',) # Barre de recherche par titre
    inlines = [ModuleInline]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'cours', 'ordre')
    list_filter = ('cours',) # Filtre sur le côté pour trier par cours
    inlines = [LeconInline]

@admin.register(Lecon)
class LeconAdmin(admin.ModelAdmin):
    list_display = ('titre', 'module', 'ordre')
    list_filter = ('module__cours',) # Filtre par cours pour trouver une leçon

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'cours', 'date_inscription')
    list_filter = ('cours', 'etudiant')

@admin.register(Progression)
class ProgressionAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'lecon', 'termine', 'date_fin')
    list_filter = ('termine', 'etudiant')

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'telephone')

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'module')