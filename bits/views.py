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

@login_required
def publicProfileViewLoggedIn(request, username):
    you = LibertasUser.objects.get(username=username)
    yourBits = Bit.objects.all().filter(sender=you.pk)
    profile_pic = you.profile_pic.url
    banner_pic = you.banner_pic.url
    followerCount = 0
    if LibertasUser.objects.filter(following=you.pk).all().exists():
        followerCount = LibertasUser.objects.filter(follower=you.pk).all().count()
    else:
        pass
    return render(request, 'bits/internalProfile.html', {'bits': yourBits, 'username': username, 'profile_pic':profile_pic, 'banner_pic':banner_pic, 'followerCount':followerCount})

def publicProfileView(request, username):
    you = LibertasUser.objects.get(username=username)
    yourBits = Bit.objects.all().filter(sender=you.pk)
    profile_pic = you.profile_pic.url
    banner_pic = you.banner_pic.url
    followerCount = 0
    if LibertasUser.objects.filter(following=you.pk).all().exists():
        followerCount = LibertasUser.objects.filter(follower=you.pk).all().count()
    else:
        pass
    return render(request, 'bits/publicProfile.html', {'bits': yourBits, 'username': username, 'profile_pic':profile_pic, 'banner_pic':banner_pic, 'followerCount':followerCount})

def getTheLatestTweetsFromFollowing(request, username):
    pass
    #TableName.objects.filter(key=value).order_by('-date_filed').first()
