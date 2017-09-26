from django.db import models

# Create your models here.
class BbqParty(models.Model):
    """
    le groupe avec le stuff en stock
    """
    def __str__(self):
        return "BbqParty"


class Commande(models.Model):
     """
     les viandes des commandes
     """
     viandeText = models.CharField(max_length=200)

     def __str__(self):
         return viandeText

class Miam(models.Model):
     """
     les viandes des commandes
     """
     viandeText = models.CharField(max_length=200)

     def __str__(self):
         return viandeText

class Participant(models.Model):
     """
     les viandes des commandes
     """
     viandeText = models.CharField(max_length=200)

     def __str__(self):
         return viandeText

class Stuff(models.Model):
    """
    Stuff donc charbon
    """
    nom = models.CharField(max_length=100)


class Boisson(models.Model):
     """
     les viandes des commandes
     """
     viandeText = models.CharField(max_length=200)

     def __str__(self):
         return viandeText
