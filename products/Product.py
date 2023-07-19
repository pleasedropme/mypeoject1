from django.db import models
import requests

class Product(models.Model):
    amazon_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField()

    def __str__(self):
        return self.title




def get_product_data(amazon_id):
    """
    Функция для получения данных о продукте с Amazon Product Advertising API.

    Входные параметры:
    - amazon_id (str): ID продукта на Amazon.

    Возвращает:
    - dict: Словарь с данными о продукте.
    """
    # URL и параметры запроса
    url = "https://api.amazon.com/product/"
    params = {
        "amazon_id": amazon_id,
    }

    # Отправляем запрос и получаем ответ
    response = requests.get(url, params=params)

    # Возвращаем данные о продукте
    return response.json()
