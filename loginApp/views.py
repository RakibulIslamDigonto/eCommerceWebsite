from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics, permissions, serializers, status, parsers, renderers, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# from otp import generate_otp
from loginApp.serializers import UserSerializer
from eCommerceWebsite import settings
from .serializers import TokenSerializer, UserSerializer
from django.db import transaction
from django.http import Http404
from django.contrib.auth import authenticate
from .models import User

class UserRegister(APIView):
    @transaction.atomic
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#signin view
class ObtainAuthToken(APIView):
    serializer_class = UserSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]


    @csrf_exempt
    def post(self, request):

        email= request.data.get('email')
        print('e======',email)
        password= request.data.get('password')
        print('ps======',password)
        user = authenticate(request, email=email, password=password)
        print("user is authenticated", user)
        if user:
            
            token, created = Token.objects.get_or_create(user=user)

            data={
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_active': user.is_active,
                'token': token.key,
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({'message':'what happend'},status=status.HTTP_400_BAD_REQUEST)


class TokenCheck(APIView):
    permission_classes = [AllowAny,]
    serializers_class = TokenSerializer

    def post(self, request, formate=None):
        token = request.data.get('token')
        token_ins = Token.objects.filter(key=token).exists()
        if token_ins:
            serializer = TokenSerializer(token_ins)
            return Response({'message': True}, status=status.HTTP_200_OK)

class Signout(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

