from django.db import models
from django.utils import timezone
from django.urls import reverse



class Post(models.Model):

#login required before post
    cover = models.ImageField(upload_to='images/', blank=False)
    title = models.CharField(max_length=50, default='')
    caption = models.TextField(max_length=200, blank=True, default='')
    birthday = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery_detail', kwargs={'pk': self.pk})


#comment
class Comment(models.Model):
    post = models.ForeignKey('gallery.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    content = models.TextField(max_length=100, blank=False, default='재미있는 사진이군요.')
    birthday = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content



