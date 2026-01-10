from django.contrib import admin
from .models import Sujet, Cours, Module, Contenu

@admin.register(Sujet)
class SujetAdmin(admin.ModelAdmin):
    list_display = ['titre', 'slug']
    prepopulated_fields = {'slug': ('titre',)}

class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ['titre', 'sujet', 'auteur', 'date_creation']
    list_filter = ['date_creation', 'sujet']
    search_fields = ['titre', 'description']
    inlines = [ModuleInline]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['titre', 'cours', 'ordre']

@admin.register(Contenu)
class ContenuAdmin(admin.ModelAdmin):
    list_display = ['titre', 'module']