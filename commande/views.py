from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from django.contrib.auth import authenticate, login, logout
from BBQ import settings
from django.contrib.auth.decorators import login_required

from .models import Commande, Participant, Produit, Evenement

@login_required
def index(request):
    # user = User.object.get()
    return render(request, 'commande/index.html')
    # return HttpResponse("Hello, world. You're at the commande index.")

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'current_commande'

    def get_queryset(self):
        """Return the last five published questions."""
        return
        Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
