from django.shortcuts import render


# Create your views here.
from core import models


def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'home.html', context)


def detail(request):
    context = {}
    return render(request, 'detail.html', context)
