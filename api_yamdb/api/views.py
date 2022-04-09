import uuid

from api.permissions import CustomIsAdmin
from api.serializers import (MeSerializer, SignUpSerializer, TokenSerializer,
                             UsersSerializer)
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from users.models import User


class SignUpAPI(APIView):

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        confirmation_code = str(uuid.uuid4())
        if serializer.is_valid():
            email = serializer.validated_data['email']
            username = serializer.validated_data['username']
            if username == 'me':
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
            send_mail(
                'Код подверждения', confirmation_code,
                ['admin@email.com'], (email, ), fail_silently=False
            )
            User.objects.create(
                username=username,
                email=email,
                confirmation_code=confirmation_code
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenAPI(APIView):

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
    permission_classes = (CustomIsAdmin, )
    filter_backends = (filters.SearchFilter, )
    filterset_fields = ('username')
    search_fields = ('username', )
    lookup_field = 'username'


class MeAPI(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = get_object_or_404(User, username=self.request.user)
        serializer = MeSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        user = get_object_or_404(User, username=self.request.user)
        serializer = MeSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
