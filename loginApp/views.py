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
        data = {
            'username': request.data.get('gmail', None),
            'password': request.data.get('password', None),
        }
        authentication = authenticate(request, username=data['username'], password=data['password'])
        if authentication:
            user = User.objects.filter(email=data['username']).first()
            if user is None:
                return Response({"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'logged_in':True, 'data': user.as_json()}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)


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

