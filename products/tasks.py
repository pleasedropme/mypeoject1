from celery import shared_task
from .models import Product
from .utils import get_product_data, translate_product_data

@shared_task
def update_product_data():
    """Обновляет данные о продуктах и переводах."""
    for product in Product.objects.all():
        # Получаем новые данные о продукте
        data = get_product_data(product.amazon_id)
        # Обновляем данные о продукте
        product.title = data['title']
        product.description = data['description']
        product.price = data['price']
        product.image_url = data['image_url']
        product.save()
        # Обновляем переводы
        translate_product_data(product)
