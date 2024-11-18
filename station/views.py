from .models import Lieu, Habitant
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DeplacerPersonnageForm


def liste_personnages(request):
    personnages = Habitant.objects.select_related('lieu')
    return render(request, 'station/liste_personnages.html', {'personnages': personnages})



def lieu_list(request):
    lieux = Lieu.objects.all()
    return render(request, 'station/lieu_list.html', {'lieux': lieux})


def details_lieu(request, lieu_id):
    lieu = get_object_or_404(Lieu, id=lieu_id)
    return render(request, 'station/details_lieu.html', {'lieu': lieu})



def vue_ensemble(request):
    lieux = Lieu.objects.prefetch_related('habitants')
    return render(request, 'station/vue_ensemble.html', {'lieux': lieux})


def details_personnage(request, personnage_id):
    personnage = get_object_or_404(Habitant, id=personnage_id)

    if request.method == 'POST':
        form = DeplacerPersonnageForm(request.POST, instance=personnage, personnage=personnage)
        if form.is_valid():
            nouveau_lieu = form.cleaned_data['lieu']
            if not nouveau_lieu.est_plein():
                form.save()
                return redirect('details_personnage', personnage_id=personnage.id)
            else:
                error_message = f"Le lieu '{nouveau_lieu.nom}' est plein."
        else:
            error_message = "Le formulaire n'est pas valide."
    else:
        form = DeplacerPersonnageForm(instance=personnage, personnage=personnage)
        error_message = None

    return render(request, 'station/details_personnage.html', {
        'personnage': personnage,
        'form': form,
        'error_message': error_message,
    })
