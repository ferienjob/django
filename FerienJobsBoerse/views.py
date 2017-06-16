from django.http import HttpResponse
from django.template import Context , loader
from django.shortcuts import render

routes = [
    {'name': 'Home', 'key': '/'},
    {'name': 'Suche', 'key': '/suche/'}
]

# def base(request):
#     return render(request, '../templates/base.html', {'message':'Hello Word 123'})

def start(request):
    return render(request, '../templates/home.html', {'routes': routes, 'current_route': '/'})
def suche(request):
    return render(request, '../templates/suche.html', {'routes': routes, 'current_route': '/suche/'})
