from django.contrib import admin
from .models import AutomatedSite

# Регистрируем модель AutomatedSite в административном интерфейсе
admin.site.register(AutomatedSite)
