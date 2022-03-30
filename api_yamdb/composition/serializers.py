from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Titles, Genres, Categories, Author


class AuthorSerializer(serializers.ModelSerializer):
    titles = serializers.SlugRelatedField(
        slug_field='title',
        many=True,
        allow_null=True,
        read_only=True
    )

    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'titles'
        )


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class TitlesSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        slug_field='slug',
        many=False,
        read_only=True
    )
    genre = serializers.StringRelatedField(
        many=False,
        read_only=True,
        allow_null=True
    )

    class Meta:
        fields = ('pk', 'title','author', 'release', 'title_urls', 'categories', 'genre')
        model = Titles
        validators = [
            UniqueTogetherValidator(
                queryset=Titles.objects.all(),
                fields=('title', 'author', 'categories')
            )
        ]