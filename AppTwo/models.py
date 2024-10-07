from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=13,null=True, blank=True)
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

class Webpage(models.Model):
    category = models.ForeignKey(Topic,on_delete=models.CASCADE) 
    name = models.CharField(max_length=264)
    url = models.URLField()

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE,)
    date = models.DateField()
    
    def __str__(self):
        return self.date
    