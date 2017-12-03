# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.username

class Poster(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name='posters',
    )
    uploaddate = models.DateTimeField(
            default=timezone.now)
    eventname = models.CharField(max_length = 50)
    eventdate = models.DateTimeField(
            blank=True, null=True)
    eventenddate = models.DateTimeField(blank=True, null=True)
    eventplace = models.CharField(max_length = 50, null=True)
    eventtext = models.TextField()
    eventholder = models.CharField(max_length = 50, null=True)
    file = models.ImageField()

