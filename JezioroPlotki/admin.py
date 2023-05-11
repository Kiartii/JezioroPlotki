from django.contrib import admin
from .models import Article
from .models import Temperature
from django.contrib.auth.models import Group

admin.site.register(Article)
admin.site.register(Temperature)

admin.site.unregister(Group)

