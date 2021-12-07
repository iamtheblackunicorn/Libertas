# Libertas by Alexander Abraham, "The Black Unicorn".
# Licensed under the MIT license.
from django.utils.translation import gettext_lazy
from django.contrib.auth.base_user import BaseUserManager
default = 'nobody@nothing.com'
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError(gettext_lazy('Field(s) must be set!'))
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, username, password, **extra_fields):
        email=default
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)
