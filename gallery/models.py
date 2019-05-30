from django.db import models
from django.utils import timezone
from django.urls import reverse



class Post(models.Model):
    cover = models.ImageField(upload_to='images/', blank=False)
    title = models.CharField(max_length=50, blank=True)
    caption = models.TextField(max_length=200, blank=True, default='')
    birthday = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'pk': self.pk})




