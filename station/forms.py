from django import forms
from .models import Habitant, Lieu

class DeplacerPersonnageForm(forms.ModelForm):
    class Meta:
        model = Habitant
        fields = ['lieu']
        labels = {
            'lieu': 'Nouveau lieu',
        }
        widgets = {
            'lieu': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        personnage = kwargs.pop('personnage')  # Récupère le personnage passé au formulaire
        super().__init__(*args, **kwargs)
        if personnage and personnage.lieu:
            # Filtre uniquement les lieux adjacents
            self.fields['lieu'].queryset = personnage.lieu.connections.all()
