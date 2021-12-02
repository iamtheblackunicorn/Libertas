from .forms import *
from .models import Bit
from django.utils.http import *
from django.utils.encoding import *
from django.shortcuts import render
from django.shortcuts import redirect
from accounts.models import LibertasUser
from django.contrib.auth.decorators import login_required

def newBit(request, username):
    if request.method == "POST":
        form = BitForm(request.POST)
        if form.is_valid():
            bitBody = form.save(commit=False)
            bitBody.sender = request.user
            bitBody.save()
            return redirect('bits:publicProfileView', username=username)
    else:
        form = BitForm()
    return render(request, 'bits/new.html', {'form': form})

def publicProfileView(request, username):
    you = LibertasUser.objects.get(username=username)
    yourBits = Bit.objects.all().filter(sender=you.pk)
    profile_pic = you.profile_pic.url
    banner_pic = you.banner_pic.url
    return render(request, 'bits/profile.html', {'bits': yourBits, 'username': username, 'profile_pic':profile_pic, 'banner_pic':banner_pic})
