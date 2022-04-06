from django.db import models
from django.contrib.auth.models import AbstractUser

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

roles = (
    (USER, 'user'),
    (MODERATOR, 'moderator'),
    (ADMIN, 'admin'),
)

class User(AbstractUser):
    password = models.CharField(max_length=50, blank=True, null=False)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField('email address', unique=True)
    role = models.CharField(choices=roles, max_length=9, default='user')
    bio = models.TextField('Биография', max_length=256)
    confirmation_code = models.CharField('Код подтверждения', max_length=100) 

    #PASSWORD_FIELD = 'email'

    def __str__(self):
        return str(self.username)