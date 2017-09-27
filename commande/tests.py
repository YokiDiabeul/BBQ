from django.test import TestCase

from .models import Produit, Commande, Participant, Evenement



# Test sur les fonctio dans les models
class ProduitMethodTest(TestCase):

    def testCalculerPrix_withPrixNegatif(self):
        """
        La fonction CaclulerPrix doit retourner 0 si prix est négatif
        """

        produit = Produit.objects.create("Boeuf", prix=-1, 0, 'v')
        self.assertEqual(produit.calculerPrix(), 0)



# Test sur les views
class LoginViewTest(TestCase):
    
