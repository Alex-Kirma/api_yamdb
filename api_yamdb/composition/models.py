from django.db import models


class Author(models.Model):
    """Модель Автор для будущих расширений"""
    first_name = models.TextField()
    last_name = models.TextField()
    slug = models.SlugField(
        max_length=80,
        unique=True
    )

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
    title = models.TextField(
        'Название произведения',
        help_text='Введите название произведения'
    )
    title_urls = models.URLField(
        unique=True,
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='titles',
        blank=True,
        null=True
    )
    release = models.DateField(
        'Дата публикации',
        help_text='Введите дату публикации')
    genre = models.ForeignKey(
        Genres,
        on_delete=models.SET_NULL,
        verbose_name='Жанр',
        help_text='Введите жанры произведения',
        null=True,
        blank=True,
        related_name='titles'
    )
    categories = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        help_text='Введите категорию произведения',
        null=False,
        blank=False,
        related_name='titles'
    )
    
    class Meta:
        ordering = ['-release']
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
