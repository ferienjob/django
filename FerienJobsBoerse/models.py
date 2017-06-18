from django.contrib.auth.models import User
from django.db import models

class Person(models.Model):
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    telephone_number = models.CharField(max_length=30)
    date_of_birth = models.CharField(max_length=30)
    qualifications = models.CharField(max_length=30)
    wish_sector = models.CharField(max_length=30)

class Company(models.Model):
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    homepage = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    telephone_number = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    image_url = models.CharField(max_length=300)

    contact_first_name = models.CharField(max_length=30)
    contact_last_name = models.CharField(max_length=30)
    contact_email = models.CharField(max_length=30)
    contact_telephone_number = models.CharField(max_length=30)
    contact_image_url = models.CharField(max_length=300)

    @classmethod
    def create(cls, data):
        company = cls(data)
        return company

class Job(models.Model):
    title = models.CharField(max_length=30)
    professional_field = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    start_date = models.CharField(max_length= 30)
    end_date = models.CharField(max_length= 30)
    start_time = models.CharField(max_length= 30)
    end_time = models.CharField(max_length= 30)
    min_age = models.CharField(max_length= 30)
    income_per_hour = models.CharField(max_length= 30)
    description = models.CharField(max_length=300)
    requirements = models.CharField(max_length= 30)
    image_url = models.CharField(max_length= 300)

    company = models.ForeignKey(
        'Company',
        # null=True,
        default=None
    )
