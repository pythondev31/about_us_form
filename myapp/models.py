from django.db import models

# # Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    company = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    # area_code = models.CharField(max_length=5)
    exist = models.CharField(max_length=3)