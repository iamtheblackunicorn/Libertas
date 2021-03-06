# Libertas by Alexander Abraham, "The Black Unicorn".
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
          'bio':'About',
          'apiAuth':'Auth',
          'profile_pic':'Profile Picture',
          'banner_pic':'Banner Picture'
        }
        fields = (
        'username',
        'bio',
        'apiAuth',
        'profile_pic',
        'banner_pic',
        )
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
class OldUserChangeForm(UserChangeForm):
    class Meta:
        model = LibertasUser
        fields = ('username',)
