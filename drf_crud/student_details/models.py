from django.db import models

# Create your models here.

class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    email = models.EmailField(max_length=254, blank=True, null=True, default=None)
    phone = models.CharField(max_length=16, blank=True, null=True, default=None)
    address = models.CharField(max_length=254, blank=True, null=True, default=None)
