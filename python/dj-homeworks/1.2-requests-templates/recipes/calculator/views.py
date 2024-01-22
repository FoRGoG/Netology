from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.core.paginator import Paginator

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
    'pureshechka': {
        'соль, г': 1,
        'молоко, мл': 250,
        'сливочное масло, г': 50,
        'картофель, кг': 1.2,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def hello(request, recipe_name):
    servings = int(request.GET.get('servings', 1))
    result = dict()
    for ingredients, amount in DATA[recipe_name].items():
        result[ingredients] = amount * servings
    context = {'recipe': result}
    return render(request, 'calculator/index.html', context)

def home_view(request):
    return HttpResponse('Hello, i want you to write some dish into the parameter')