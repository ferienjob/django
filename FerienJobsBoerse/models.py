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

    # - - old - - #
    # day_of_birth = models.CharField(max_length=10)
    # email = models.CharField(max_length=30)
    # password = models.CharField(max_length=101)
    # description = models.CharField(max_length=256)
    # image = models.CharField(max_length=23)


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

    # - - old - - #
    # date = models.CharField(max_length=10)
    # phone_number = models.CharField(max_length=20)
    # fax_number = models.CharField(max_length=20)
    # email = models.CharField(max_length=30)
    # image = models.CharField(max_length=23)

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

    # - - old - - #
    # date = models.CharField(max_length=10)
    # from_to_date =models.CharField(max_length=23)
    # image = models.CharField(max_length=23)
