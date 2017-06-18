from django.http import HttpResponse
from django.template import Context , loader
from django.shortcuts import render, redirect
# from django.http import JsonResponse
from django.http import HttpResponse, JsonResponse
import json

import FerienJobsBoerse.models as models

routes = [
    {'name': 'Home', 'key': '/'},
    {'name': 'Suche', 'key': '/suche/'}
]
branchen = [
    {'name': '... in allen', 'key': 'alle'},
    {'name': '... in Gastronomie', 'key': 'gastronomie'},
    {'name': '... in IT', 'key': 'it'},
    {'name': '... in Handwerk', 'key': 'handwerk'},
    {'name': '... in Tourismus', 'key': 'tourismus'},
    {'name': '... in Handel', 'key': 'handel'},
    {'name': '... in Bauwesen', 'key': 'bauwesen'},
    {'name': '... in Soziales', 'key': 'soziales'},
    {'name': '... in Offentlicher Dienst', 'key': 'offentlicher_dienst'},
    {'name': '... in Industrie', 'key': 'industrie'},
    {'name': '... in Umwelt', 'key': 'umwelt'},
    {'name': '... in Logistik', 'key': 'logistik'},
    {'name': '... in Erziehung', 'key': 'erziehung'},
    {'name': '... in Bildung', 'key': 'bildung'},
    {'name': '... in Marketing', 'key': 'marketing'}
]


def home(request):
    count = models.Job.objects.raw('''
        SELECT id, COUNT(*) AS count
        FROM FerienJobsBoerse_job
    ''')[0].count

    jobs = models.Job.objects.raw('''
        SELECT
        	`FerienJobsBoerse_job`.`id`,
            `FerienJobsBoerse_job`.`title` as job_title,
            `FerienJobsBoerse_job`.`description` as job_description,
            `FerienJobsBoerse_company`.`id` as company_id,
            `FerienJobsBoerse_company`.`name` as company_name

        FROM `FerienJobsBoerse_job`


        INNER JOIN `FerienJobsBoerse_company`
        ON `FerienJobsBoerse_job`.company_id = `FerienJobsBoerse_company`.id

        WHERE `FerienJobsBoerse_job`.id = 1
        LIMIT 4
    ''')

    # return render(request, '../templates/home.html', {'routes': routes, 'current_route': '/'})
    return render(
        request,
        'landing_page.html',
        {
            'routes': routes,
            'current_route': '/',
            'count': count,
            'jobs': jobs
        }
    )



def suche(request):
    # Find multiple jobs by title & city
    job_title = request.GET.get('title', '')
    branche = request.GET.get('branche', '')
    ort = request.GET.get('ort', '')

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
        SELECT
            *,
            `FerienJobsBoerse_company`.`id` as company_id,
            `FerienJobsBoerse_company`.`name` as company_name,

            `FerienJobsBoerse_company`.`contact_first_name`,
            `FerienJobsBoerse_company`.`contact_last_name`,
            `FerienJobsBoerse_company`.`contact_email`,
            `FerienJobsBoerse_company`.`contact_telephone_number`,
            `FerienJobsBoerse_company`.`contact_image_url`

        FROM FerienJobsBoerse_job

        INNER JOIN `FerienJobsBoerse_company`
        ON `FerienJobsBoerse_job`.company_id = `FerienJobsBoerse_company`.id

        WHERE `FerienJobsBoerse_job`.id = %s
        LIMIT 1
    ''', [int(id)])[0]

    # contact_first_name = models.CharField(max_length=30)
    # contact_last_name = models.CharField(max_length=30)
    # contact_email = models.CharField(max_length=30)
    # contact_telephone_number = models.CharField(max_length=30)
    # contact_image_url = models.CharField(max_length=300)

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

def take_over_company(request, id):
    request.session['company_id'] = int(id)
    company = models.Job.objects.raw('''
        SELECT * FROM FerienJobsBoerse_company
        WHERE id = %s
    ''', [int(id)])[0]

    request.session['company_name'] = company.name

    # return HttpResponse(id)
    return redirect('/firmen/')



def list_companies(request):
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

        company_id = request.session.get('company_id', None)
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
