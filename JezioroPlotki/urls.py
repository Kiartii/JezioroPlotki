"""
URL configuration for JezioroPlotki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

handler404 = views.handler404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('obszar-natura-2000/', views.obszar_natura_2000, name='obszar-natura-2000'),
    path('hydrobiologia/', views.hydrobiologia, name='hydrobiologia'),
    path('hydrologia-jeziora/', views.hydrologia_jeziora, name='hydrologia-jeziora'),
    path('partnerzy/', views.partnerzy, name='partnerzy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)