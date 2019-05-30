from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    body = models.TextField()
    update_date = models.DateTimeField(auto_now=True) 