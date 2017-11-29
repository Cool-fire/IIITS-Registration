# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def get_upload_path(instance,filename):
    return 'documents/{0}/{1}'.format(instance.user,filename)


class Document(models.Model):
    user = models.CharField(max_length=200,null=True)
    time = models.CharField(max_length=800,null=True)
    docfile = models.FileField(upload_to=get_upload_path)

    def __str__(self):
        return self.user
class Documentone(models.Model):
    user = models.CharField(max_length=200,null=True)
    time = models.CharField(max_length=800,null=True)
    docfile1 = models.FileField(upload_to=get_upload_path)

    def __str__(self):
        return self.user