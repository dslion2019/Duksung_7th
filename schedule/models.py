from django.db import models

# Create your models here.
class Schedule(models.Model):
    title = models.CharField(max_length=50)
    #start_date = models.fields.DateTimeField()
    #end_date = models.fields.DatetTimeField()