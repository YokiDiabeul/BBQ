from django.contrib import admin
from . import models

@admin.register(models.CommandeTotal)
class CommandeTotalAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Nourriture)
class NourritureAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Boisson)
class BoissonAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Stuff)
class StuffAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Participant)
class ParticipantAdmin(admin.ModelAdmin):
    pass
