from django.db import models

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
