from django.db import models
from django.contrib.auth.models import User

# Modèle pour les Cours
class Cours(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='cours/', blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

#pour les Modules (un cours a plusieurs modules)
class Module(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='modules')
    titre = models.CharField(max_length=200)
    ordre = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.cours.titre} - {self.titre}"

# Modèle pour les Leçons (
class Lecon(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lecons')
    titre = models.CharField(max_length=200)
    contenu_texte = models.TextField(blank=True)
    video_url = models.URLField(blank=True)
    ordre = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titre

# Modèle pour les Inscriptions
class Inscription(models.Model):
    etudiant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mes_inscriptions')
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.etudiant.username} inscrit à {self.cours.titre}"

# Modèle pour la Progression__Suivre les cours
class Progression(models.Model):
    etudiant = models.ForeignKey(User, on_delete=models.CASCADE)
    lecon = models.ForeignKey(Lecon, on_delete=models.CASCADE)
    termine = models.BooleanField(default=False)
    date_fin = models.DateTimeField(auto_now=True)

# Modèle pour les Évaluations 
class Evaluation(models.Model):
    module = models.OneToOneField(Module, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)

    def __str__(self):
        return self.titre
    

class Profil(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profils/', blank=True)
    # Relation vers les cours suivis
    cours_suivis = models.ManyToManyField(Cours, blank=True, related_name='etudiants')
    
    def __str__(self):
        return f"Profil de {self.utilisateur.username}"

# Nouveau modèle pour enregistrer les notes aux évaluations
class ResultatEvaluation(models.Model):
    etudiant = models.ForeignKey(User, on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    note = models.FloatField()
    date_passage = models.DateTimeField(auto_now_add=True)