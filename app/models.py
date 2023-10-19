from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    img = models.ImageField(null=True,upload_to='img')
    time = models.TimeField(auto_now=False, auto_now_add=True,null=True)
    date = models.DateField(auto_now=False, auto_now_add=True,null=True)