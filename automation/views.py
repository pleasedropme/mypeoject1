from django.shortcuts import render
from .models import Site
from products.views import update_product_data_automatically
from translations.views import update_translations_automatically
from django.shortcuts import render
from .tasks import run_automation

def run_automation_view(request):
    """Запускает автоматическое обновление данных о продуктах и переводах и отображает результаты."""
    results = run_automation.delay()
    return render(request, 'automation/results.html', {'results': results})


# Функция представления для отображения списка сайтов
def site_list(request):
    sites = Site.objects.all()  # Получаем все сайты из базы данных
    return render(request, 'automation/site_list.html', {'sites': sites})


def create_site(request):
    """
    Функция представления для создания нового сайта.

    Входные параметры:
    - request (HttpRequest): Объект запроса Django.

    Возвращает:
    - HttpResponse: Объект ответа Django.
    """
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        url = request.POST.get('url')

        # Создаем новый сайт
        site = Site(name=name, url=url)
        site.save()

        return render(request, 'automation/site_created.html', {'site': site})

    return render(request, 'automation/create_site.html')



def automate_site_creation_and_updates():
    """
    Функция для автоматического создания и обновления сайтов, продуктов и переводов.

    Возвращает:
    - dict: Словарь с созданными и обновленными объектами.
    """
    # Создаем новые сайты
    new_sites = []
    for i in range(5):
        name = f"Site {i+1}"
        url = f"https://www.site{i+1}.com"
        new_site = create_site_automatically(name, url)
        new_sites.append(new_site)

    # Обновляем данные о продуктах и переводах
    updated_products = update_product_data_automatically()
    updated_translations = update_translations_automatically()

    return {
        "new_sites": new_sites,
        "updated_products": updated_products,
        "updated_translations": updated_translations,
    }




def automation_results(request):
    """
    Функция представления для отображения результатов автоматизации.

    Входные параметры:
    - request (HttpRequest): Объект запроса Django.

    Возвращает:
    - HttpResponse: Объект ответа Django.
    """
    # Получаем результаты автоматизации
    results = automate_site_creation_and_updates()

    # Отображаем результаты на веб-сайте
    return render(request, 'automation/results.html', results)
