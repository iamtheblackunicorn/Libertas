# Libertas by Alexander Abraham, "The Black Unicorn".
# Licensed under the MIT license.
from django import forms
from .models import Bit
class BitForm(forms.ModelForm):
    #subject = forms.CharField(label='New Bit', max_length=2000 , widget=forms.TextInput(attrs={'class':'newBit'}))
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
        #self.fields['bitBody'].attrs['class'] = 'newBit'
