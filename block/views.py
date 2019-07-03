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
      form.save()nothing to commit, working tree clean
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

def biz_details(request):
  user = request.user
  hood = Neighbourhood.objects.get(admin=user)
  print(hood)

  if request.method == 'POST':
    bizform= BusinessForm(request.POST)
    if bizform.is_valid():
      bform = bizform.save(commit=False)
      bform.person= user
      bform.bizhood= hood
      bform.save()
    return redirect('home',hood.id)
  else:
    bizform = BusinessForm()
  return render(request, 'enter_biz.html',{'bizform':bizform}) 

