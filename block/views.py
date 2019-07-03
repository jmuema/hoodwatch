# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from. models import * 

# Create your views here.
def register(request):
  if request.method == 'POST':
    form = UserRegistrationFOrm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      return redirect('login')

  else:
    form = UserRegistrationFOrm()
    return render(request, 'users/register.html', {'form' : form})

def profile(request):
  user = request.user
  profiles = Profile.objects.all()
  hood = Neighbourhood.objects.filter(admin=user.id)
  return render(request, 'profile.html', {'profiles': profiles, 'user':user, 'hood':hood})

def hood_details(request):
  user= request.user
  if request.method == 'POST':
    hoodform = NeighbourhoodForm(request.POST)
    if hoodform.is_valid():
      hform = hoodform.save(commit=False)
      hform.admin = user
      hform.save()
    return redirect('profile')
  else:
    hoodform = NeighbourhoodForm()
  return render(request, 'enter_hood.html',{'hoodform':hoodform})

# @login_required
def home(request,id):
  user = request.user
  hood = Neighbourhood.objects.get(id=id)
  biz = Business.objects.filter(bizhood=hood.id)
  return render(request,'home.html',{'hood':hood,'biz':biz,'user':user})

    