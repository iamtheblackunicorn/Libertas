# Krypton by Alexander Abraham, "The Black Unicorn".
# Licensed under the MIT license.

from django import forms
from .models import LibertasUser
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = LibertasUser
        labels = {
          'username':'Username',
          'apiAuth':'App password',
          'profile_pic':'Profile Picture',
          'banner_pic':'Banner Picture'
        }
        fields = (
        'username',
        'apiAuth',
        'profile_pic',
        'banner_pic',
        )
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
        #self.fields['profile_pic'].required = False
        #self.fields['banner_pic'].required = False

class OldUserChangeForm(UserChangeForm):
    class Meta:
        model = LibertasUser
        fields = ('username',)
