from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.db.models import Q

from .models import Haiku
from .forms import ModelHaikuForm


def index(request):
    haiku_qs = Haiku.objects.all()

    context = {
        'haiku_qs': haiku_qs,
    }

    return render(request, 'index.html', context)

def detailed(request, title_obj):
    haiku = Haiku.objects.get(url_title=title_obj)

    context = {
        'haiku': haiku,
    }

    return render(request, 'detailed.html', context)
