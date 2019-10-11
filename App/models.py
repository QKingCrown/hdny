from django.db import models

# Create your models here.
class Master(models.Model):
    name = models.CharField(max_length=20)
    money = models.CharField(max_length=20)
    first_time = models.DateField()
    number = models.CharField(max_length=20)