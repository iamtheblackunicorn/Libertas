# Libertas by Alexander Abraham, "The Black Unicorn".
# Licensed under the MIT license.
from . import views
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
app_name = 'bits'
urlpatterns = [
    path('timeline', views.getTheLatestTweetsFromFollowing, name='timeline'),
    path('<str:username>', views.publicProfileView, name='publicProfileView'),
    path('bitActionLike/<int:bitPk>', views.likeBit, name='likeBit'),
    path('bitActionReBit/<int:bitPk>', views.reBit, name='reBit'),
    path('profile/<str:username>/new', views.newBit, name='newBit'),
    path('profile/<str:username>', views.publicProfileViewLoggedIn, name='internalProfileView'),
    # 127.0.0.1:8000/api/user/lol21/following
    path('api/user/<str:apiKey>/following/', views.getApiBits, name='getApiBits'),
    # 127.0.0.1:8000/api/user/lol21
    path('api/user/<str:apiKey>', views.apiUserProfile, name='apiUserProfile'),
    # 127.0.0.1:8000/api/user/lol21/new/I_sent_this_via_the_API_!
    path('api/user/<str:apiKey>/new/<str:message>', views.apiNewBit, name='apiNewBit')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
