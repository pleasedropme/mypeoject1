from django.shortcuts import render
from .models import Product

# Функция представления для отображения списка продуктов
def product_list(request):
    products = Product.objects.all()  # Получаем все продукты из базы данных
    return render(request, 'products/product_list.html', {'products': products})


def update_product_data(amazon_id):
    """
    Функция для обновления данных о продукте.

    Входные параметры:
    - amazon_id (str): ID продукта на Amazon.

    Возвращает:
    - Product: Обновленный объект продукта.
    """
    # Получаем данные о продукте с Amazon
    data = get_product_data(amazon_id)

    # Обновляем данные о продукте в базе данных
    product = Product.objects.get(amazon_id=amazon_id)
    product.title = data['title']
    product.description = data['description']
    product.price = data['price']
    product.image_url = data['image_url']
    product.save()

    return product


def update_product_data_automatically():
    """
    Функция для автоматического обновления данных о всех продуктах.

    Возвращает:
    - list: Список обновленных объектов продуктов.
    """
    updated_products = []

    # Обновляем данные о каждом продукте
    for product in Product.objects.all():
        updated_product = update_product_data(product.amazon_id)
        updated_products.append(updated_product)

    return updated_products
