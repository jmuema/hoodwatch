from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:     #gives us a nested name space for configs and keeps them in 1 place
        model = User
        fields = ['username','email','password1','password2']

class EditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_pic']

class HoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['admin']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'neighbourhood']

class BusinessForm(forms.ModelForm):
    class Meta:
            model = Business
            exclude = ['neighbourhood', 'profile']
class NewCommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    exclude = ['post','postername','pub_date']
