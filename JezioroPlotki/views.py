from django.shortcuts import render
from .models import Article
from .models import Temperature


def index(request):
    articles = Article.objects.filter(category='Strona-Glowna')
    temp = Temperature.objects.last()
    context = {'articles': articles,
               'temperature': temp}
    return render(request, 'index.html', context)


def info(request):
    articles = Article.objects.filter(category='Informacje')
    context = {'articles': articles}
    return render(request, 'info.html', context)


def obszar_natura_2000(request):
    articles = Article.objects.filter(category='Obszar-Natura-2000')
    context = {'articles': articles}
    return render(request, 'obszar-natura-2000.html', context)


def hydrobiologia(request):
    articles = Article.objects.filter(category='Hydrobiologia')
    context = {'articles': articles}
    return render(request, 'hydrobiologia.html', context)


def hydrologia_jeziora(request):
    articles = Article.objects.filter(category='Hydrologia-Jeziora')
    context = {'articles': articles}
    return render(request, 'hydrologia-jeziora.html', context)


def partnerzy(request):
    return render(request, 'partnerzy.html')


def handler404_view(request, exception):
    return render(request, '404.html', status=404)


def galeria(request):
    return render(request, 'galeria.html')
