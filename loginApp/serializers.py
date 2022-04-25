from sqlite3.dbapi2 import IntegrityError

from django.contrib.auth import authenticate

from django.db import models, transaction
from django.db.models import fields
from django.utils.crypto import get_random_string

from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
# from otp import generate_otp
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'is_active', 'birthday', 'gender', 'profession', 'verification_code')
        extra_kwargs = {'password':{'write_only':True}}


class TokenSerializer(AuthTokenSerializer):
    pass





