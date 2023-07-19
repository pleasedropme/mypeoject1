from django.contrib import admin
from .models import Product

# Регистрируем модель Product в административном интерфейсе
admin.site.register(Product)
