from django.db import models
from django_countries.fields import CountryField
# Create your models here.


class user_data(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class Person(models.Model):
    name=models.CharField(max_length=100)
    lastname = models.CharField(max_length=50)
    country = CountryField()