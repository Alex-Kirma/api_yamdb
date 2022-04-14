from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import UsernameValidator

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'


class User(AbstractUser):

    roles = (
        (USER, USER),
        (MODERATOR, MODERATOR),
        (ADMIN, ADMIN),
    )
    username_validator = UsernameValidator()
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True
    )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField('Email', max_length=254, unique=True)
    role = models.CharField(
        'Роль пользователя',
        choices=roles,
        max_length=len(MODERATOR), default=USER
    )
    bio = models.TextField('Биография', blank=True)
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=100,
        null=True
    )

    REQUIRED_FIELDS = ["email"]
    USERNAME_FIELDS = "email"

    def __str__(self):
        return str(self.username)
