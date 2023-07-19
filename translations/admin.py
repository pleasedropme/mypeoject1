from django.contrib import admin
from .models import Translation

# Регистрируем модель Translation в административном интерфейсе
admin.site.register(Translation)
