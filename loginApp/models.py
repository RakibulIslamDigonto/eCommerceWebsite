from distutils.command.build_scripts import first_line_re
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy

# create auto profile by signal
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('User must have an email')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self._create_user(email, password, **extra_fields)


class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name=ugettext_lazy('email address'), max_length=255, unique=True)
    is_active = models.BooleanField(default=True, help_text=ugettext_lazy('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    is_staff = models.BooleanField(default=False, help_text=ugettext_lazy('Designates whether the user can log into this admin site.'))


    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    country= models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''if first_name and last_name not show should be (self.user)'''
        return self.first_name + ' ' + self.last_name + 's profile'

    def is_full_filled(self):
        fields_name = [f.name for f in self._meta.get_fields()]

        for field in fields_name:
            if getattr(self, field) == '':
                return False
        return True





    




