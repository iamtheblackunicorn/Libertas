# Libertas by Alexander Abraham, "The Black Unicorn".
# Licensed under the MIT license.
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
class LibertasUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=300,unique=True)
    apiAuth = models.CharField(max_length=16,unique=True)
    follower = models.ForeignKey(to='LibertasUser',on_delete=models.CASCADE,related_name='followerNew', null=True, blank=True)
    following = models.ForeignKey(to='LibertasUser',on_delete=models.CASCADE,related_name='followingNew', null=True, blank=True)
    profile_pic = models.ImageField(upload_to='images/profile_pictures')
    banner_pic = models.ImageField(upload_to='images/banner_pictures')
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.username
