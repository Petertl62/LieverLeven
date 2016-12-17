from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.db.models import Q

from .models import Evenement
from .forms import ModelInschijfForm


def index(request):
    evenement_qs = Evenement.objects.all()

    context = {
        'evenement_qs': evenement_qs,
    }

    return render(request, 'evenement_index.html', context)

def detailed(request, title_obj):
    evenement = Evenement.objects.get(url_title=title_obj)

    context = {
        'evenement': evenement,
    }

    return render(request, 'evenement_detailed.html', context)

def inschrijven(request, title_obj):
    evenement = Evenement.objects.get(url_title=title_obj)

    if request.POST:
        form = ModelInschijfForm(request.POST)
        if form.is_valid():
            inschrijving = form.save(commit=False)
            inschrijving.evenement = evenement
            inschrijving.save()
            return redirect('/evenementen/%s/' %(evenement.url_title))
    else:
        form = ModelInschijfForm()

    context = {
        'evenement': evenement,
        'form': form,
    }

    return render(request, 'evenement_inschrijven.html')
