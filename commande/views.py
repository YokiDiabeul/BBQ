from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import Boisson, Nourriture, CommandeTotal, Participant, Stuff

# Create your views here.
# class IndexView(generic.ListView):
#     template_name = 'index.html'
#     context_object_name = '??????'
#     def login():
#         #if islogged() :
#         return HttpResponseRedirect(reverse('commande:index', args=(question.id,)))

def index(request):
    return HttpResponse("Hello, world. You're at the commande index.")
