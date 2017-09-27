from django.contrib import admin
from . import models

@admin.register(models.Commande)
class CommandeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Produit)
class ProduitAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Evenement)
class EvenementAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Participant)
class ParticipantAdmin(admin.ModelAdmin):
    pass
