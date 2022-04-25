from distutils.command.build_scripts import first_line_re
from statistics import mode
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy
from django.conf import settings
from rest_framework.authtoken.models import Token


# create auto profile by signal
from django.db.models.signals import post_save
from django.dispatch import receiver
import jwt
from datetime import datetime, timedelta


class CustomUserManager(BaseUserManager):
    # use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if email is None:
            raise ValueError('The given email must be set')

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        #when user is created,and until mail funtionality work add, set is_active to false
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        if password is None:
            raise TypeError('Superusers must have a password.')

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=254,
        unique=True,
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    verification_code = models.CharField(max_length=10, blank=True, null=True)


    # EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.admin

    def as_json(self):
        token, created = Token.objects.get_or_create(user=self)
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_active": self.is_active,
            "token": token.key,
        }





































# class MyUserManager(BaseUserManager):
#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('User must have an email')

#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
        
#         return self._create_user(email, password, **extra_fields)


# class MyUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(verbose_name=gettext_lazy('email address'), max_length=255, unique=True)
#     is_active = models.BooleanField(default=True, help_text=gettext_lazy('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
#     is_staff = models.BooleanField(default=False, help_text=gettext_lazy('Designates whether the user can log into this admin site.'))


#     USERNAME_FIELD = 'email'
#     objects = MyUserManager()

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_staff

#     def full_name(self):
#         return self.email

#     def get_short_name(self):
#         return self.email

#     @property
#     def token(self):
#         token = jwt.encode({
#             'email': self.email,
#             'exp': datetime.utcnow() + timedelta(hours=24)}, settings.SECRET_KEY, algorithm='HS256')
#         return token




# class Profile(models.Model):
#     user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='profile')
#     first_name = models.CharField(max_length=50, blank=True)
#     last_name = models.CharField(max_length=50, blank=True)
#     country= models.CharField(max_length=50, blank=True)
#     address = models.CharField(max_length=100, blank=True)
#     city = models.CharField(max_length=50, blank=True)
#     zipcode = models.CharField(max_length=10, blank=True)
#     phone = models.CharField(max_length=20, blank=True)
#     join_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         '''if first_name and last_name not show should be (self.user)'''
#         return self.first_name + ' ' + self.last_name + 's profile'

#     def is_full_filled(self):
#         fields_name = [f.name for f in self._meta.get_fields()]

#         for field in fields_name:
#             if getattr(self, field) == '':
#                 return False
#         return True

# @receiver(post_save, sender=MyUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=MyUser)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()