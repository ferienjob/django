from django.http import HttpResponse
from django.template import Context , loader
from django.shortcuts import render
# from django.http import JsonResponse
from django.http import HttpResponse, JsonResponse
import json

import FerienJobsBoerse.models as models

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

    branchen = [
        {'name': '... in allen', 'key': 'alle'},
        {'name': '... in Gastronomie', 'key': 'gastronomie'}
    ]

    jobs = models.Job.objects.raw('SELECT * FROM FerienJobsBoerse_job')

    return render(
        request,
        '../templates/suche.html',
        {
            'routes': routes,
            'current_route': '/suche/',

            'branchen': branchen,
            'jobs': jobs,

            'current_job_title': job_title,
            'current_branche': branche,
            'current_ort': ort
        }
    )


def job(request, id):
    # Find Job by id
    # job = next((x for x in jobs if x['id'] == int(id)), None)
    job = models.Job.objects.raw('''
        SELECT * FROM FerienJobsBoerse_job
        WHERE id = %s
        LIMIT 1
    ''', [int(id)])[0]

    return render(
        request,
        '../templates/job.html',
        {
            'id': id,
            'routes': routes,
            'current_route': '/job/',

            'job': job
        }
    )

def firmen(request):
    firmen = models.Job.objects.raw('''
        SELECT * FROM FerienJobsBoerse_company
    ''')
    current_firma_id = request.session.get('company_id', None)
    return render(
        request,
        '../templates/_firmen.html',
        {'firmen': firmen, 'current_firma_id': current_firma_id}
    )

def serve_create_company(request):
    return render(
        request,
        '../templates/Registrieren_Firmen.html',
        {}
    )

def serve_create_job(request):
    if request.session.get('company_id', False):
        return render(
            request,
            '../templates/Job_hinzufuegen.html',
            {}
        )
    else:
        return HttpResponse('You need to be a company to create job')

def create_job(request):
    params = request.GET

    job = models.Job(
        title = params.get('title', ''),
        professional_field = params.get('professional_field', ''),
        address = params.get('address', ''),
        start_date = params.get('start_date', ''),
        end_date = params.get('end_date', ''),
        start_time = params.get('start_time', ''),
        end_time = params.get('end_time', ''),
        min_age = params.get('min_age', ''),
        income_per_hour = params.get('income_per_hour', ''),
        description = params.get('description', ''),
        requirements = params.get('requirements', ''),
        image_url = params.get('image_url', ''),
    )
    job.save()
    return HttpResponse(job.id)

def create_company(request):
    params = request.GET

    company = models.Company(
        email = params.get('email', ''),
        password = params.get('password', ''),
        name = params.get('name', ''),
        homepage = params.get('homepage', ''),
        address = params.get('address', ''),
        telephone_number = params.get('telephone_number', ''),
        description = params.get('description', ''),
        image_url = params.get('image_url', ''),

        contact_first_name = params.get('contact_first_name', ''),
        contact_last_name = params.get('contact_last_name', ''),
        contact_email = params.get('contact_email', ''),
        contact_telephone_number = params.get('contact_telephone_number', ''),
        contact_image_url = params.get('contact_image_url', ''),
    )
    company.save()

    request.session['company_id'] = company.id

    return HttpResponse(company.id)

# def login(request):
#     return render(request, '../templates/login.html', {})

# def company(request):
#     return render(request, '../templates/company.html', {})
