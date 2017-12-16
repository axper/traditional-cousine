from django.shortcuts import render


# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)


def detail(request):
    context = {}
    return render(request, 'detail.html', context)
