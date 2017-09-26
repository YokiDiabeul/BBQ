from django.db import models

# Create your models here.
class Nourriture(models.Model):
    """ la bouffe """
    nom = models.CharField(max_length=50)
    prix = models.IntegerField(blank=False, null=False)
    quantite = models.IntegerField(null=False)
    commandeTotal = models.ForeignKey(
        CommandeTotal,
        on_delete=SET_NULL,
        blank=True,
        null=True,
        related_name='nourritures')

    def __str__(self):
         return self.nom

class Boisson(models.Model):
    """ la boisson """
    nom = models.CharField(max_length=50)
    prix = models.IntegerField(blank=False, null=False)
    quantite = models.IntegerField(null=False)
    commandeTotal = models.ForeignKey(
        CommandeTotal,
        on_delete=SET_NULL,
        blank=True,
        null=True,
        related_name='boissons')

    def __str__(self):
      return self.nom

class Stuff(models.Model):
    """ le stuff """
    nom = models.CharField(max_length=50)
    prix = models.IntegerField(blank=False, null=False)
    quantite = models.IntegerField(null=False)

    def __str__(self):
        return self.nom

class Participant(models.Model):
    """ les gens """
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    solde = models.FloatField()
    commandeTotal = models.ForeignKey(
        CommandeTotal,
        on_delete=SET_NULL,
        blank=True,
        null=True,
        related_name='participants')


    def __str__(self):
        return self.nom + self.prenom

class CommandeTotal(models.Model):
    """ la CommandeTotal """
    date = models.DateTimeField('date du bbq')

    def __str__(self):
        return date
