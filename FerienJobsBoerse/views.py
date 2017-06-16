from django.http import HttpResponse
from django.template import Context , loader
from django.shortcuts import render
import django.FerienJobsBoerse.models as models
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

def login(request):
    return render(request, '../templates/login.html', {models.Person.email,models.Person.password})