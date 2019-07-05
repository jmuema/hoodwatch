# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.

class UserTest(TestCase):
    def setUp(self):
        self.user=User(username='Joseph',first_name='Muema',last_name='Mwangangi',email='jmuema95@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))

    def test_data(self):
        self.assertTrue(self.user.username,"Joseph")
        self.assertTrue(self.user.first_name,"Muema")
        self.assertTrue(self.user.last_name,'Mwangangi')
        self.assertTrue(self.user.email,'jmuema95@gmail.com')

    def test_save(self):
        self.user.save()
        users = User.objects.all()
        self.assertTrue(len(users)>0)

    def test_delete(self):
        user = User.objects.filter(id=1)
        user.delete()
        users = User.objects.all()
        self.assertTrue(len(users)==0)