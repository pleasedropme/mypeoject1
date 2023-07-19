from django.shortcuts import render
from .models import Translation
import requests

# Функция представления для отображения перевода продукта
def translation_detail(request, product_id, language):
    translation = Translation.objects.get(product_id=product_id, language=language)  # Получаем перевод продукта из базы данных
    return render(request, 'translations/translation_detail.html', {'translation': translation})



def translate_text(text, target_language):
    """
    Функция для перевода текста с помощью Google Translate API.

    Входные параметры:
    - text (str): Текст для перевода.
    - target_language (str): Язык, на который нужно перевести текст.

    Возвращает:
    - str: Переведенный текст.
    """
    # URL и параметры запроса
    url = "https://api.google.com/translate/"
    params = {
        "text": text,
        "target_language": target_language,
    }

    # Отправляем запрос и получаем ответ
    response = requests.get(url, params=params)

    # Возвращаем переведенный текст
    return response.text





def update_translation(product_id, language):
    """
    Функция для обновления перевода продукта.

    Входные параметры:
    - product_id (int): ID продукта.
    - language (str): Язык перевода.

    Возвращает:
    - Translation: Обновленный объект перевода.
    """
    # Получаем продукт и его перевод
    product = Product.objects.get(id=product_id)
    translation = Translation.objects.get(product_id=product_id, language=language)

    # Обновляем перевод
    translation.title = translate_text(product.title, language)
    translation.description = translate_text(product.description, language)
    translation.save()

    return translation


def update_translations_automatically():
    """
    Функция для автоматического обновления всех переводов.

    Возвращает:
    - list: Список обновленных объектов переводов.
    """
    updated_translations = []

    # Обновляем каждый перевод
    for translation in Translation.objects.all():
        updated_translation = update_translation(translation.product_id, translation.language)
        updated_translations.append(updated_translation)

    return updated_translations
