from django.db import models
from django.utils import timezone



class Post(models.Model):
    cover = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    caption = models.TextField(max_length=200, blank=True, default='hack your life')
    now = timezone.now()

    def __str__(self):
        return self.title

