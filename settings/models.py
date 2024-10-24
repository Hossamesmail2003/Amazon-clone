from django.db import models

# Create your models here.
class company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company')
    subtitle = models.TextField(max_length=500)
    facebook_link = models.URLField(max_length=200,null=True,blank=True)
    twitter_link = models.URLField(max_length=200,null=True,blank=True)
    youtube_link = models.URLField(max_length=200,null=True,blank=True)
    phones = models.TextField(max_length=500,null=True,blank=True)
    email = models.TextField(max_length=500,null=True,blank=True)
    address= models.TextField(max_length=500,null=True,blank=True)
    android_app = models.URLField(max_length=200,null=True,blank=True)
    ios_app = models.URLField(max_length=200,null=True,blank=True)
    call_us= models.TextField(max_length=100,null=True,blank=True)
    email_us= models.TextField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name
    

