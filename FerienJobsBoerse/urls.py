
"""FerienJobsBoerse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from FerienJobsBoerse import views

urlpatterns = [
    url(r'^admin/', (admin.site.urls)),
    url(r'^$' ,views.home),
    url(r'^suche/' ,views.suche),
    # url(r'^login/' ,views.login),
    url(r'^job/(?P<id>\d+)/$', views.job),

    url(r'^add/job/$', views.serve_create_job),
    url(r'^create_job/$', views.create_job),

    url(r'^add/firma/$', views.serve_create_company),
    url(r'^create_company/$', views.create_company), # form
    url(r'^firmen/$', views.list_companies),

    url(r'^take_over/company/(?P<id>\d+)/$', views.take_over_company),

    # url(r'^company/' ,views.company),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
print(settings.STATIC_URL, settings.STATIC_ROOT)
