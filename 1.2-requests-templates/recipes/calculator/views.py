from django.shortcuts import render
import re

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def home_view(request):
    """ Стартовая страница """
    template_name = 'calculator/home.html'
    pages = {
        'Омлет': 'omlet/?servings=1',
        'Паста': 'pasta/?servings=1',
        'Бутерброд': 'buter/?servings=1'
    }
    context = {'pages': pages}
    return render(request, template_name, context)


def recipes(request, recipe):
    """ Отображает количество ингредиентов. """
    servings = request.GET.get('servings', 1)
    ingredients = DATA.get(recipe, {}).copy()
    if recipe in DATA:
        for ingr in ingredients:
            ingredients[ingr] *= int(servings)
        context = {'recipe': ingredients}
    else:
        context = {}
    return render(request, 'calculator/index.html', context)
