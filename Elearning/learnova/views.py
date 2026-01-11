from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Profil, Cours, Module, Lecon, Evaluation,ResultatEvaluation
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def page_des_cours(request):
    tous_les_cours = Cours.objects.all()
    return render(request, 'liste_cours.html', {'cours_liste': tous_les_cours})

def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # On crée le profil lié à cet utilisateur immédiatement
            Profil.objects.create(utilisateur=user) 
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'inscription.html', {'form': form})

# CORRECTION ICI : Ajout de get_object_or_404
def detail_cours(request, cours_id):
    cours = get_object_or_404(Cours, id=cours_id)
    modules = cours.modules.all().order_by('ordre')
    return render(request, 'detail_cours.html', {'cours': cours, 'modules': modules})

# CORRECTION ICI : Ajout de get_object_or_404
def afficher_lecon(request, lecon_id):
    lecon = get_object_or_404(Lecon, id=lecon_id)
    return render(request, 'lecon.html', {'lecon': lecon})


@login_required
def voir_profil(request):
    # On essaie de récupérer le profil, sinon on le crée
    profil, created = Profil.objects.get_or_create(utilisateur=request.user)
    
    mes_cours = profil.cours_suivis.all()
    mes_resultats = ResultatEvaluation.objects.filter(etudiant=request.user).order_by('-date_passage')
    
    return render(request, 'profil.html', {
        'profil': profil,
        'mes_cours': mes_cours,
        'mes_resultats': mes_resultats
    })

def faire_evaluation(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    evaluation = get_object_or_404(Evaluation, module=module)
    # On récupère toutes les questions de cette évaluation
    questions = evaluation.questions.all() 
    
    if request.method == 'POST':
        # Ici on traitera les réponses plus tard
        pass

    return render(request, 'evaluation.html', {
        'module': module,
        'evaluation': evaluation,
        'questions': questions
    })