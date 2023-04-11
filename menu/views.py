from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def homepage(request):
    return render(request, 'menu/home.html')


def activate_menu(request, slug):
    obj = Menu.objects.get(slug=slug)

    context = {
        "obj": obj,
        "items": obj.children.all(),
    }

    return render(request, 'menu/activate_menu.html', context=context)
