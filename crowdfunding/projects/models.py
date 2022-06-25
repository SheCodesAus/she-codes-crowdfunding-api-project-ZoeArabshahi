from email.mime import image
from turtle import title
from unittest.util import _MAX_LENGTH
from xml.etree.ElementTree import Comment
from django.db import models

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
        )
    supporter = models.CharField(max_length=200)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField()
    goal=models.IntegerField()
    image=models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.CharField(max_length=200)

