# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Neighbourhood(models.Model):
  hood_name = models.CharField(max_length =50)
  hood_location = models.CharField(max_length =50)
  occupants = models.IntegerField(blank=True, null=True)
  admin = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__ (self):
    return self.hood_name

  def save_neighbourhood(self):
    self.save()


