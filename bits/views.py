from .forms import *
from django.db import models
from .models import Bit
from .models import BitLike
from django.utils.http import *
from django.utils.encoding import *
from django.shortcuts import render
from django.http import JsonResponse
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
    bio = LibertasUser.objects.get(username=username).bio
    followerCount = 0
    followingCount = 0
    bitLikeDict = []
    for i in bits:
        bitPk = i.pk
        bitText = i.bitBody
        bitSender = i.sender.username
        likeCount = BitLike.objects.filter(bitData=Bit.objects.get(pk=bitPk)).all().count()
        if likeCount:
            bitLikeDict = bitLikeDict + [[bitText,likeCount,bitSender,bitPk]]
        else:
            bitLikeDict = bitLikeDict + [[bitText,likeCount,bitSender,bitPk]]
    followerCount = LibertasUser.objects.filter(following=alien.pk).all().count()
    followingCount = LibertasUser.objects.filter(follower=alien.pk).all().count()
    print(bitLikeDict)
    return render(request, 'bits/internalProfile.html', {'bits': bitLikeDict, 'bio':bio, 'username': username, 'profile_pic':profile_pic, 'banner_pic':banner_pic, 'followerCount':followerCount, 'followingCount':followingCount, 'loggedInUserName':loggedInUser})


@login_required
def likeBit(request, bitPk):
    liker = LibertasUser.objects.get(username=request.user.username)
    bitToLike = Bit.objects.get(pk=bitPk)
    bitOwner = Bit.objects.get(pk=bitPk).sender
    try:
        newLike = BitLike(bitData=bitToLike, userWhoLiked=liker)
        newLike.save()
        print('Success!')
        return redirect('bits:internalProfileView', username=bitOwner)
    except Exception as error:
        print(str(error))
        return redirect('accounts:dashboard', username=liker.username)
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
    profile_pic = request.user.profile_pic.url
    bitList = []
    you = LibertasUser.objects.get(username=username)
    allUsersFollowed = LibertasUser.objects.all().filter(follower=you.pk)
    for i in allUsersFollowed:
        userObject = i
        bitterProfilePic = userObject.profile_pic.url
        bit = Bit.objects.filter(sender=userObject.pk).order_by('date').first()
        likeCount = BitLike.objects.filter(bitData=bit).all().count()
        bitList = bitList + [[bit.bitBody, bit.sender, bit.pk, likeCount, bitterProfilePic]]
    print(bitList)
    return render(request, 'bits/timeline.html', {'bits':bitList, 'username':username, 'profile_pic':profile_pic})
@login_required
def publicProfileView(request, username):
    alien = LibertasUser.objects.get(username=username)
    bio = LibertasUser.objects.get(username=username).bio
    bits = Bit.objects.all().filter(sender=alien.pk)
    profile_pic = alien.profile_pic.url
    banner_pic = alien.banner_pic.url
    followerCount = 0
    followingCount = 0
    bitLikeDict = []
    for i in bits:
        bitPk = i.pk
        bitText = i.bitBody
        bitSender = i.sender.username
        likeCount = BitLike.objects.filter(bitData=Bit.objects.get(pk=bitPk)).all().count()
        if likeCount:
            bitLikeDict = bitLikeDict + [[bitText,likeCount,bitSender,bitPk]]
        else:
            bitLikeDict = bitLikeDict + [[bitText,likeCount,bitSender,bitPk]]
    followerCount = LibertasUser.objects.filter(following=alien.pk).all().count()
    followingCount = LibertasUser.objects.filter(follower=alien.pk).all().count()
    return render(request, 'bits/publicProfile.html', {'bits': bitLikeDict, 'bio':bio, 'username': username, 'profile_pic':profile_pic, 'banner_pic':banner_pic, 'followerCount':followerCount, 'followingCount':followingCount})

def apiUserProfile(request,apiKey):
    try:
        origin = request.get_host()
        user = LibertasUser.objects.get(apiAuth=apiKey)
        username = user.username
        userProfilePic = origin + user.profile_pic.url
        userBannerPic = origin + user.banner_pic.url
        userBits = Bit.objects.all().filter(sender=user.pk)
        responseList = []
        for i in userBits:
            bitBody = i.bitBody
            bitDate = i.date
            responseList = responseList + [[bitBody, bitDate]]
        response = {
            apiKey:[username,userProfilePic, userBannerPic],
            'bits':responseList
        }
        return JsonResponse(response)
    except Exception as error:
        print(str(error))
        response = {'404':'Error'}
        return JsonResponse(response)

def getApiBits(request,apiKey):
    try:
        origin = request.get_host()
        you = LibertasUser.objects.get(apiAuth=apiKey)
        followingUsers = LibertasUser.objects.all().filter(following=you)
        response = {}
        for i in followingUsers:
            alienUserName = i.username
            alienProfilePicture = origin + i.profile_pic.url
            alienBitList = []
            alienBits = Bit.objects.all().filter(sender=i)
            for alienBit in alienBits:
                alienBitBody = alienBit.bitBody
                alienBitDate = alienBit.date
                alienBitList = alienBitList + [[alienBitBody, alienBitDate]]
            response[alienUserName] = [
                {'profile_pic':alienProfilePicture,'bits':alienBitList}
            ]
        return JsonResponse(response)
    except Exception as error:
        print(str(error))
        response = {'404':'Error'}
        return JsonResponse(response)

def apiNewBit(request,apiKey, message):
    try:
        body = ' '.join(message.split('_'))
        newBit = Bit(
            bitBody=body,
            sender=LibertasUser.objects.get(apiAuth=apiKey),
            date=models.DateTimeField(verbose_name='date',auto_now=True)
        )
        newBit.save()
        response = {'200':'OK'}
        return JsonResponse(response)
    except Exception as error:
        print(str(error))
        response = {'500':'Error'}
        return JsonResponse(response)
