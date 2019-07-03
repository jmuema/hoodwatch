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

class Profile(models.Model):
    me = models.OneToOneField(User,on_delete=models.CASCADE)
    myhood = models.ForeignKey(Neighbourhood)
    profile_image = models.ImageField(default='default.jpeg')

    def __str__(self):
      return f"{self.me.username}'s Profile"

    def save_profile(self):
      self.save()

class Business(models.Model):
  person = models.ForeignKey(User)
  bizname = models.CharField(max_length =50)
  bizpost = models.CharField(max_length =500, blank=True, null=True)
  email = models.CharField(max_length = 50)
  bizhood = models.ForeignKey(Neighbourhood)

  def save_business(self):
    self.save()

  def __str__(self):
    return f"{self.person.username}'s Post"

  @classmethod
  def search_by_bizname(cls.bizname):
    searched = cls.obects.filter(bizname_icontains=bizname)
    return searched

  
