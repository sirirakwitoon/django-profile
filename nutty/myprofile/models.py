from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=50)
    tel = models.CharField(max_length=100)
    facebook_url = models.CharField(max_length=100)
    instagram_url = models.CharField(max_length=100)
    github_url = models.CharField(max_length=100)


class Subscriberlist(models.Model):
    email = models.CharField(max_length=50)
