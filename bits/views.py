from .forms import *
from django.db import models
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
            return redirect('bits:internalProfileView', username=username)
    else:
        form = BitForm()
    return render(request, 'bits/new.html', {'form': form})
@login_required
def publicProfileViewLoggedIn(request, username):
    loggedInUser = request.user.username
    alien = LibertasUser.objects.get(username=username)
    bits = Bit.objects.all().filter(sender=alien.pk)
    profile_pic = alien.profile_pic.url
    banner_pic = alien.banner_pic.url
    followerCount = 0
    followingCount = 0
    followerCount = LibertasUser.objects.filter(following=alien.pk).all().count()
    followingCount = LibertasUser.objects.filter(follower=alien.pk).all().count()
    return render(request, 'bits/internalProfile.html', {'bits': bits, 'username': username, 'profile_pic':profile_pic, 'banner_pic':banner_pic, 'followerCount':followerCount, 'followingCount':followingCount, 'loggedInUserName':loggedInUser})
@login_required
def likeBit(request, bitPk):
    userWhoLiked = request.user
    bitToLike = Bit.objects.get(pk=bitPk)
    bitOwner = Bit.objects.get(pk=bitPk).sender.username
    try:
        bitToLike.like = request.user
        bitToLike.save()
        print('Success!')
        return redirect('bits:internalProfileView', username=bitOwner)
    except Exception as error:
        print(str(error))
        return redirect('accounts:dashboard', username=userWhoLiked.username)
@login_required
def reBit(request, bitPk):
    currentUser = request.user
    originalUser = Bit.objects.get(pk=bitPk).sender
    newBit = Bit(
        bitBody=Bit.objects.get(pk=bitPk).bitBody,
        bitPic=Bit.objects.get(pk=bitPk).bitPic,
        sender=currentUser,
        date=models.DateTimeField(verbose_name='date',auto_now=True)
    )
    try:
        newBit.save()
        return redirect('bits:internalProfileView', username=originalUser)
    except Exception as error:
        print(str(error))
        return redirect('accounts:dashboard', username=currentUser.username)
@login_required
def getTheLatestTweetsFromFollowing(request):
    username = request.user.username
    bitList = []
    you = LibertasUser.objects.get(username=username)
    allUsersFollowed = LibertasUser.objects.all().filter(follower=you.pk)
    for i in allUsersFollowed:
        userObject = i
        bitList = bitList + [Bit.objects.filter(sender=userObject.pk).order_by('date').first()]
    return render(request, 'bits/timeline.html', {'content':bitList, 'username':username})
def publicProfileView(request, username):
    alien = LibertasUser.objects.get(username=username)
    bits = Bit.objects.all().filter(sender=alien.pk)
    profile_pic = alien.profile_pic.url
    banner_pic = alien.banner_pic.url
    followerCount = 0
    followingCount = 0
    followerCount = LibertasUser.objects.filter(following=alien.pk).all().count()
    followingCount = LibertasUser.objects.filter(follower=alien.pk).all().count()
    return render(request, 'bits/publicProfile.html', {'bits': bits, 'username': username, 'profile_pic':profile_pic, 'banner_pic':banner_pic, 'followerCount':followerCount, 'followingCount':followingCount})
