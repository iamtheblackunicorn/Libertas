# Krypton by Alexander Abraham, "The Black Unicorn".
# Licensed under the MIT license.

from django import forms
from .models import Bit

class BitForm(forms.ModelForm):
    class Meta:
        model = Bit
        labels = {
            'bitBody':'Your Bit',
            'bitPic':'Add an image'
        }
        fields = ('bitBody','bitPic')
    def __init__(self, *args, **kwargs):
        super(BitForm, self).__init__(*args, **kwargs)
        self.fields['bitPic'].required = False
