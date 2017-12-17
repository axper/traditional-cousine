from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

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


def subscribe(request):
    if request.method != "POST":
        return redirect(to='core:home')
    email = request.POST['email']
    if not email:
        return HttpResponse(content='email cannot be empty', status=400)
    print('Subscribed email: ' + email)
    content = '<p>Welcome to Hamegh!</p>' \
        '<p>You have successfully subscribed to our recipes! If you have any further questions, ' \
        'please feel free to contact us via hamegh-help@lazydevelo.com</p>' \
        'Thank you!<br>' \
        '<center style="color:#606060">' \
        'Copyright © {% now "Y" %} The Hamegh Team. All rights reserved.<br>' \
        'You are receiving this email because you subscribed to Hamegh via our web ' \
        'interface.</center>'
    send_mail(
        'You have successfully subscribed to Hamegh',
        content,
        'no-reply@hamegh.com',
        [email],
        fail_silently=False,
    )
    return redirect(to='core:home')
