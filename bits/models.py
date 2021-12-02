from django.db import models
from accounts.models import LibertasUser

class Bit(models.Model):
    bitBody = models.CharField(max_length=200000)
    bitPic = models.ImageField(verbose_name='bitPic', upload_to='images/bit_pictures', null=True, blank=True)
    sender = models.ForeignKey(LibertasUser,on_delete=models.CASCADE,related_name='sender')
    date = models.DateTime(verbose_name='date',auto_now=True)
    def __str__(self):
        return bitBody
