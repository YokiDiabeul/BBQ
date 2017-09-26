from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from django.contrib.auth import authenticate, login, logout
from BBQ import settings
from django.contrib.auth.decorators import login_required

from .models import Boisson, Nourriture, CommandeTotal, Participant, Stuff

@login_required
def index(request):
    # user = User.object.get()
    return render(request, 'commande/index.html')
    # return HttpResponse("Hello, world. You're at the commande index.")
