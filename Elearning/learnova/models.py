from django.db import models
from django.contrib.auth.models import User

class Sujet(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Sujet"
        verbose_name_plural = "Sujets"

    def __str__(self):
        return self.titre

class Cours(models.Model):
    auteur = models.ForeignKey(User, related_name='cours_crees', on_delete=models.CASCADE)
    sujet = models.ForeignKey(Sujet, related_name='cours', on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    
    # Gestion des inscriptions
    eleves = models.ManyToManyField(User, related_name='cours_rejoints', blank=True)

    class Meta:
        verbose_name = "Cours"
        verbose_name_plural = "Cours"

    def __str__(self):
        return self.titre

class Module(models.Model):
    cours = models.ForeignKey(Cours, related_name='modules', on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    ordre = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"

    def __str__(self):
        return f"{self.ordre}. {self.titre}"

class Contenu(models.Model):
    module = models.ForeignKey(Module, related_name='contenus', on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    corps = models.TextField() 

    class Meta:
        verbose_name = "Contenu"
        verbose_name_plural = "Contenus"