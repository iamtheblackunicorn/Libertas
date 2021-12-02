# Libertas by Alexander Abraham, "The Black Unicorn".
# Licensed under the MIT license.
from . import views
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
app_name = 'bits'
urlpatterns = [
    path('profile/<str:username>/new', views.newBit, name='newBit'),
    path('profile/<str:username>', views.publicProfileView, name='publicProfileView'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
