from http.client import HTTPResponse
from django.shortcuts import render

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
    # можете добавить свои рецепты ;)
}

def omlet(request):
    servings = int(request.GET.get('servings', 1))
    
    recip_omlet = {} 
    for key, values in DATA['omlet'].items():
        recip_omlet[key] = values * servings
    
    context = {
        'title': f'Рецепт омлета на {servings} персоны(у)',
        'recipe': recip_omlet
    }
    
    return render(request, 'calculator/index.html', context)

def pasta(request):
    servings = int(request.GET.get('servings', 1))
    
    recip_pasta = {}   
    
    for key, values in  DATA['pasta'].items():
        recip_pasta[key] = values * servings
    
    context = {
       'title': f'Рецепт пасты на {servings} персоны(у)',
       'recipe': recip_pasta
    }
    
    return render(request, 'calculator/index.html', context)