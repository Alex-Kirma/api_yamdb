from django.db import models


class Author(models.Model):
    """Модель Автор для будущих расширений"""
    first_name = models.TextField
    last_name = models.TextField
    slug = models.SlugField

    def __str__(self) -> str:
        return self.slug


class Genres(models.Model):
    """Модель жанры, мнгое кмногому"""
    genre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField

    def __str__(self):
        return self.slug


class Categories(models.Model):
    """Модель категории одно к многим """
    category = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    description = models.TextField

    def __str__(self) -> str:
        return self.slug


class Titles(models.Model):
    """Модель Произведение, базовая модель"""
    title = models.TextField
    title_urls = models.URLField(
        unique=True,
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='title',
        blank=True,
        null=True
    )
    relese = models.DateField('Дата публикации')
    genre = models.ForeignKey(
        Genres,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='title'
    )
    categories = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='title'
    )
    
    class Meta:
        ordering = -['release']
