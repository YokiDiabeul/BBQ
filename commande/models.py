from django.db import models

# Create your models here.
class BbqParty(models.Model):
    """
    le groupe avec le stuff en stock
    """
    

    def __str__(self):
        return u"BbqParty"


class Commande(models.Model):
     """
     les viandes des commandes
     """
     viandeText = models.CharField(max_length=200)
     pubDate = models.DateTimeField('date published')

     def __str__(self):
         if len(self.exempleText) > 10:
             return self.exempleText[:11] + '...'
         return self.exempleText

class Miam(models.Model):

class Participant(models.Model):

class Stuff(models.Model):
    nom = models.CharField(max_length=100)


class Boisson(models.Model):
