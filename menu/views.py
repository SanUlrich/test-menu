from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'menu/home.html')


def activate_menu(request, slug):
    return render(request, 'menu/home.html', context={"slug": slug})
