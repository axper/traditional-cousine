from django.shortcuts import render

from core import models
from core.models import Step, Recipe


def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'home.html', context)


def detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    steps = Step.objects.filter(recipe__id=recipe_id).order_by('order')
    context = {
        'recipe': recipe,
        'steps': steps,
    }
    return render(request, 'detail.html', context)


def step(request, recipe_id, order):
    step_obj = Step.objects.get(recipe__id=recipe_id, order=order)
    context = {
        'step': step_obj,
    }
    return render(request, 'step.html', context)


def about(request):
    return render(request, 'about.html')
