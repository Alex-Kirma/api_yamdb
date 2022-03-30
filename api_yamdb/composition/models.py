# from django.contrib.auth import get_user_model
from unicodedata import category
from django.db import models


class Author(models.Model):
    first_name = models.TextField
    last_name = models.TextField
    slug = models.SlugField

    def __str__(self) -> str:
        return self.slug


class Genres(models.Model):
    genre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField

    def __str__(self):
        return self.slug


class Categories(models.Model):
    category = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    description = models.TextField

    def __str__(self) -> str:
        return self.slug


class Titles(models.Model):
    title = models.TextField
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='title',
        blank=True,
        null=True
    )
    relese = models.DateField('Дата публикации')
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE, null=False, blank=False)
    
