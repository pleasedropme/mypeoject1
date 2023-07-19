from celery import shared_task
from products.tasks import update_product_data
from translations.tasks import update_translation_data

@shared_task
def run_automation():
    """Запускает автоматическое обновление данных о продуктах и переводах."""
    update_product_data.delay()
    update_translation_data.delay()
