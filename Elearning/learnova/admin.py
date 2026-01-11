from django.contrib import admin
from .models import Profil, Cours, Module, Lecon, Evaluation, ResultatEvaluation, Inscription, Progression

# --- Gestion des Leçons à l'intérieur des Modules ---
class LeconInline(admin.TabularInline):
    model = Lecon
    extra = 1  # Permet d'ajouter une leçon vide directement depuis le module

# --- Gestion des Modules à l'intérieur des Cours ---
class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1

# --- Configuration de l'affichage du Profil ---
@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'get_cours_count')
    search_fields = ('utilisateur__username',)

    def get_cours_count(self, obj):
        return obj.cours_suivis.count()
    get_cours_count.short_description = "Nombre de cours suivis"

# --- Configuration du Cours ---
@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('titre',)
    search_fields = ('titre',)
    inlines = [ModuleInline] # On peut créer les modules direct dans le cours

# --- Configuration du Module ---
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'cours', 'ordre')
    list_filter = ('cours',)
    inlines = [LeconInline] # On peut créer les leçons direct dans le module

# --- Configuration de la Leçon ---
@admin.register(Lecon)
class LeconAdmin(admin.ModelAdmin):
    list_display = ('titre', 'module')
    list_filter = ('module__cours', 'module')


@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'cours', 'date_inscription')
    list_filter = ('cours', 'etudiant')

@admin.register(Progression)
class ProgressionAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'lecon', 'termine', 'date_fin')
    list_filter = ('termine', 'etudiant')

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'module')

@admin.register(ResultatEvaluation)
class ResultatEvaluationAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'evaluation', 'note', 'date_passage')
    list_filter = ('evaluation', 'date_passage')


























