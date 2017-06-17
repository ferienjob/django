from django.contrib.auth.models import User
from django.db import models

class Person(models.Model):
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    telephone_number = models.CharField(max_length=30)
    date_of_birth = models.CharField(max_length=30)
    qualifications = models.CharField(max_length=30)
    wish_sector = models.CharField(max_length=30)

class Company(models.Model):
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    homepage = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    telephone_number = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    image_url = models.CharField(max_length=30)

    contact_first_name = models.CharField(max_length=30)
    contact_last_name = models.CharField(max_length=30)
    contact_email = models.CharField(max_length=30)
    contact_telephone_number = models.CharField(max_length=30)
    contact_image_url = models.CharField(max_length=30)

    @classmethod
    def create(cls, data):
        company = cls(data)
        # try:
        #     company = cls(data)
        # except:
        #     print "Unexpected error:", sys.exc_info()[0]
        #     raise

        return company

class Job(models.Model):
    title = models.CharField(max_length=30)
    professional_field = models.CharField(max_length=30)
    address = models.CharField(max_length= 30)
    start_date = models.CharField(max_length= 30)
    end_date = models.CharField(max_length= 30)
    start_time = models.CharField(max_length= 30)
    end_time = models.CharField(max_length= 30)
    min_age = models.CharField(max_length= 30)
    income_per_hour = models.CharField(max_length= 30)
    description = models.CharField(max_length=256)
    requirements = models.CharField(max_length= 30)
    image_url = models.CharField(max_length= 30)

class Link(models.Model):
    url = models.URLField(unique=1)

    def __unicode__(self):
        return self.title

class Lesezeichen(models.Model):
    title =  models.CharField(max_length=200)
    benutzer = models.ForeignKey(User)
    link = models.ForeignKey(Link)

    def __unicode__(self):
        return self.title


