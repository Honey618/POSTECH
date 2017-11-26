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
        related_name='poster',
    )
    uploaddate = models.DateTimeField(
            default=timezone.now)
    eventname = models.CharField(max_length = 50)
    eventdate = models.DateTimeField(
            blank=True, null=True)
    eventtext = models.TextField()
    file = models.ImageField()
    top = models.IntegerField(default = 0)
    left = models.IntegerField(default = 0)
    width = models.IntegerField(default = 200)
    height = models.IntegerField(default = 350)