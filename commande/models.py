from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Participant(models.Model):
    """ Le peule """
    # You can't get a null user
    user = models.OneToOneField(User, null=True, blank=False)
    soldes = models.FloatField(blank=False, null=True)

    def __str__(self):
        return self.user.username

class Evenement(models.Model):
    """ L'evenement """
    date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    prixTotal = models.FloatField(blank=False, null=True)
    participants = models.ManyToManyField(Participant)

    def __str__(self):
        nb = len(self.participants.all())
        return self.date.__str__() + " : " + self.prixTotal.__str__() + "€ : " + nb.__str__()


class Produit(models.Model):
    """ La boisson """
    nom = models.CharField(max_length=100, unique=True)
    prix = models.FloatField(blank=False, null=False)
    stock = models.IntegerField(blank=True, null=True)
    typeP = models.CharField(max_length=100,null=True, blank=False)
    def __str__(self):
        return self.nom + "( "+self.typeP+" ) : " + self.prix.__str__() + "€ : "+ self.stock.__str__()+"/u"

    def _calculPrix(self, quantite):
        return self.quantite * self.prix.__str__()

class Commande(models.Model):
    """ La commande """
    quantite = models.IntegerField(blank=True, null=True)
    prod = models.OneToOneField("Produit", unique=True)

    def __str__(self):
        return self.prod.__str__() + " " + self.quantite.__str__() + "/u"
