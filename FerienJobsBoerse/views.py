from django.http import HttpResponse

test1 = 'gasfsa'

def index(request):
    return HttpResponse(test1)
