# Libertas by Alexander Abraham, "The Black Unicorn".
# Licensed under the MIT license.
from django.urls import path
from django.urls import include
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('bits.urls'))
]
