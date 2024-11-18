from django.db import models

class Lieu(models.Model):
    nom = models.CharField(max_length=100, unique=True)  
    description = models.TextField(blank=True)  
    capacite_max = models.PositiveIntegerField() 
    connections = models.ManyToManyField('self', symmetrical=True, blank=True)  
    photo = models.ImageField(upload_to='photos_lieux/', blank=True, null=True)  # Nouveau champ

    def __str__(self):
        return self.nom

    def habitants_actuels(self):
        return self.habitants.count()

    def est_plein(self):
        return self.habitants_actuels() >= self.capacite_max
    
    def lieux_connectes(self):
        return self.connections.all()


class Habitant(models.Model):
    nom = models.CharField(max_length=100, unique=True)  
    description = models.TextField(blank=True)  
    etat = models.CharField(
        max_length=50,
        choices=[
            ('actif', 'Actif'),
            ('reposé', 'Reposé'),
            ('fatigué', 'Fatigué'),
            ('affamé', 'Affamé'),
        ],
        default='actif')
    lieu = models.ForeignKey(Lieu, on_delete=models.SET_NULL, null=True, related_name='habitants')
    photo = models.ImageField(upload_to='photos_personnages/', blank=True, null=True)  # Nouveau champ



    def __str__(self):
        return f"{self.nom} ({self.etat})"
    
    def changer_de_lieu(self, nouveau_lieu):
        if not nouveau_lieu.est_plein():
            self.lieu = nouveau_lieu
            self.save()
            return True
        return False
