from urllib import request
import uuid

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from api.permissions import CustomIsAdmin
from api.serializers import SignUpSerializer, TokenSerializer, UsersSerializer#, UsernameSerializer
from reviews.models import User


class SignUp(viewsets.ModelViewSet):
    queryset  = User.objects.all()
    serializer_class = SignUpSerializer
        
    #def get_queryset(self):
    #    user = get_object_or_404(User, username=self.request.user.username)
    #    queryset = User.objects.all().filter(username=user)
    #    print(1111111111, user, queryset)
    #    return queryset
    
    def perform_create(self, serializer):
        confirmation_code = str(uuid.uuid4())
        #username = serializer.validated_data['username']
        email = serializer.validated_data['email']
        #user_base = get_object_or_404(User, username = username)
        print(email, self.request.user)
        send_mail('Код подверждения', confirmation_code, email, ['admin@email.com'], fail_silently=False)
        return serializer.save(confirmation_code=confirmation_code)

class APIToken(APIView):
    queryset  = User.objects.all()
    serializer_class = TokenSerializer

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data['username']
        confirmation_code = serializer.data['confirmation_code']
        user_base = get_object_or_404(User, username=username)
        if confirmation_code == user_base.confirmation_code:
            token = str(AccessToken.for_user(user_base))
            return Response({'token': token}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    pagination_class = PageNumberPagination
    #permission_classes = (IsAdminUser,)
    #permission_classes = (CustomIsAdmin, )
    #lookup_field = 'username'
    

class UsernameViewSet(viewsets.ModelViewSet):
    #queryset = User.objects.all()
    serializer_class = UsersSerializer
    #permission_classes = (IsAdminUser,)
    #permission_classes = (CustomIsAdmin, )

    def get_queryset(self):
        user=get_object_or_404(User, username=self.kwargs.get('username'))
        print(self.kwargs.get('username'), user.email)
        queryset = User.objects.all().filter(username=user)
        return queryset

    