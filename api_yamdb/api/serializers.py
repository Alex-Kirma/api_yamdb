from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User


class SignUpSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(User.objects.all())],
        required=True
    )
    username = serializers.CharField(
        validators=[UniqueValidator(User.objects.all())],
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'email')


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )


class MeSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
