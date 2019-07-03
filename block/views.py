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
  
    