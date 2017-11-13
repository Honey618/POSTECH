from django.db import models
from django.utils import timezone


class Person(models.Model):
    user_nickname = models.CharField(max_length = 50)
    user_id = models.CharField(max_length = 50)
    
class Poster(models.Model):
    participant = models.ForeignKey(Person)
    uploaddate = models.DateTimeField(
            default=timezone.now)
    eventname = models.CharField(max_length = 50)
    eventdate = models.DateTimeField(
            blank=True, null=True)
    eventtext = models.TextField()