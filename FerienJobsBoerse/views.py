from django.http import HttpResponse
from django.template import Context , loader
from django.shortcuts import render

def base(request):
    return render(request, '../templates/base.html', {'message':'Hello Word 123'})

def start(request):
    return render(request, '../templates/start.html', {'message':'Hello Word 123'})
def suche(request):
    return render(request, '../templates/suche.html', {'message':'Hello Word 123'})
