from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Produit(models.Model):
    """ La boisson """
    nom = models.CharField(max_length=100, unique=True)
    prix = models.FloatField(blank=False, null=False)
    stock = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nom + " : " + self.prix + " : "+ self.stock

    def _calculPrix(self, quantite):
        return quantite * prix

class Commande(models.Model):
    """ La commande """
    quantite = models.IntegerField(blank=True, null=True)

class Participant(models.Model):
    """ Le peule """
    ref_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=False,
        null=False,
        related_name='user')

    soldes = models.FloatField(blank=False, null=True)


class Evenement(models.Model):
    """ L'evenement """
    date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    prixTotal = models.FloatField(blank=False, null=True)
    participants = models.ManyToManyField(Participant)
