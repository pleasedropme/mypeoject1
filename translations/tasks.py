from celery import shared_task
from .models import Translation
from .utils import translate_text

@shared_task
def update_translation_data():
    """Обновляет данные о переводах.

    Возвращает:
    - dict: Словарь с обновленными объектами.
    """
    # Получаем все объекты Translation
    translations = Translation.objects.all()

    # Обновляем данные о переводах
    for translation in translations:
        translation.title = translate_text(translation.product.title, translation.language)
        translation.description = translate_text(translation.product.description, translation.language)
        translation.save()

    return {'updated_translations': len(translations)}
