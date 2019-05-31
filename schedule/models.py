from django.db import models

# Create your models here.


class Schedule(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()