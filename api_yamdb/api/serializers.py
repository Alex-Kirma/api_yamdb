import email
from typing_extensions import Required
from urllib import request
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from reviews.models import User


class SignUpSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    confirmation_code =serializers.CharField(required = False)
    #def create(self, validated_data):
    #    
    #    user = validated_data['username']
    #    email = validated_data['email']
    #    #confirmation_code = '1111'
    #    confirmation_code = validated_data['confirmation_code']
    #    user_base = User.objects.create(username = user, email = email, confirmation_code = confirmation_code)
    #    return user_base

    class Meta:
        model = User
        fields = ('username', 'email', 'confirmation_code')
        

class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')    


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')


#class UsernameSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = User
#        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')

