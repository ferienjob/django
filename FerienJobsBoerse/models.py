from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    day_of_birth = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=101)
    description = models.CharField(max_length=256)
    image = models.CharField(max_length=23)


class Company(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=256)
    date = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    fax_number = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=101)
    image = models.CharField(max_length=23)

    @classmethod
    def create(cls, data):
        company = cls(data)
        # do something with the book
        return company

class Job(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=256)
    min_age = models.CharField(max_length= 2)
    date = models.CharField(max_length=10)
    from_to_date =models.CharField(max_length=23)
    image = models.CharField(max_length=23)
