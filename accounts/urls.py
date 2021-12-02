# Libertas by Alexander Abraham, "The Black Unicorn".
# Licensed under the MIT license.
from . import views
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.homeView, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('deleteaccount/', views.delete_user, name='deleteaccount'),
    path('dashboard/<str:username>', views.dashboard, name='dashboard'),
    path('profileAction/follow/<str:username>', views.followRequest, name='followUser')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
