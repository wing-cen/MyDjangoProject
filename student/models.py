from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=16)
    age = models.IntegerField(16)
    password = models.CharField(max_length=32)
    statue = models.IntegerField(16)

    def __unicode__(self):
        return self.name


class Wing(models.Model):
    name =  models.CharField(max_length=16)
    age = models.IntegerField(16)
    favourite = models.CharField(max_length=64)
    skill = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name