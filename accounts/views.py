# Libertas by Alexander Abraham, "The Black Unicorn".
# Licensed under the MIT license.
from .forms import *
from django import forms
from bits.models import Bit
from django.utils.http import *
from django.utils.encoding import *
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from accounts.models import LibertasUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site

def homeView(request):
    return render(request, 'accounts/home.html')
def register_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect('accounts:dashboard', username=username)
        else:
            print(form.errors)
            pwd_one = form.cleaned_data.get('password1')
            pwd_two = form.cleaned_data.get('password2')
    form = NewUserForm
    return render(request, 'accounts/register.html', context={'form':form})
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username =form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:dashboard', username=username)
            else:
                pass
        else:
            pass
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})
@login_required
def logout_user(request):
    logout(request)
    return redirect('accounts:home')
@login_required
def delete_user(request):
    username = request.user.username
    u = LibertasUser.objects.get(username=username)
    u.delete()
    return redirect('accounts:home')
@login_required
def followRequest(request, username):
    # Adri is logged in, following alexandera21
    # username = alexandera21 (alien)
    # request.user.username = adri (ME)
    you = LibertasUser.objects.get(username=request.user.username)
    alienUser = LibertasUser.objects.get(username=username)
    try:
        you.following = alienUser
        you.save()
        alienUser.follower = you
        alienUser.save()
        return redirect('bits:internalProfileView', username=username)
    except Exception as error:
        return redirect('accounts:dashboard', username=you.username)
@login_required
def dashboard(request, username):
    username = request.user.username
    apiAuth = request.user.apiAuth
    profile_pic = request.user.profile_pic.url
    banner_pic = request.user.banner_pic.url
    bio = request.user.bio
    bits = Bit.objects.all().filter(sender=request.user.pk)
    return render(request, 'accounts/dashboard.html', {'username':username, 'bio':bio, 'apiAuth':apiAuth, 'profile_pic':profile_pic, 'bits':bits, 'banner_pic':banner_pic})
