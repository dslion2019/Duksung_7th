from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    body = models.TextField()
    TITLE = (('01','멋사MT'), ('02', '아이디어톤'), ('03', '해커톤'), ('04', '세션'), ('05', '기타'))
    
    title = models.CharField(max_length=2, choices=TITLE)

    update_date = models.DateTimeField(auto_now=True) 

    def ___str___(self):
        return self.title