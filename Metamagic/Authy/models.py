from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Book(models.Model):
#     title = models.models.CharField(max_length=100)
#     author = models.models.CharField(max_length=100)

class File(models.Model):
    filepath = models.CharField(max_length=250)
    metadata = models.JSONField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)