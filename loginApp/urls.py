from django.urls import path, include
from django.contrib import admin
from .views import UserRegister, ObtainAuthToken, TokenCheck, Signout


app_name='loginApp'

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', ObtainAuthToken.as_view(), name='login'),
    path('token-check/', TokenCheck.as_view(), name='token_check'),
    path('signout', Signout.as_view(), name='signout')
]