from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def info(request):
    return render(request, 'info.html')
def hydrobiologia(request):
    return render(request, 'hydrobiologia.html')
def hydrologia_jeziora(request):
    return render(request, 'hydrologia-jeziora.html')
def partnerzy(request):
    return render(request, 'partnerzy.html')