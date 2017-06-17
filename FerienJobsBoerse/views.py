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


def home(request):
    return render(request, '../templates/home.html', {'routes': routes, 'current_route': '/'})


def suche(request):
    # Find multiple jobs by title & city
    job_title = request.GET.get('title', '')
    branche = request.GET.get('branche', '')
    ort = request.GET.get('ort', '')

    print(job_title, branche, ort)

    return render(request, '../templates/suche.html', {'routes': routes, 'current_route': '/suche/'})


def job(request, id):
    # Find Job by id

    return render(request, '../templates/job.html', {'id': id, 'routes': routes, 'current_route': '/job/'})


def login(request):
    return render(request, '../templates/login.html', {models.Person.email,models.Person.password})
