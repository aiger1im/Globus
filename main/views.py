from django.shortcuts import render

from main.models import Menu


def home(request):
    menu = Menu.objects.all()

    context = {
        'menu': menu ,
    }
    return render(request, 'main/index.html', context=context)