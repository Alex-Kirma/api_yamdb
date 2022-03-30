from platform import release
from django.contrib import admin

from .models import Author, Genres, Titles, Categories


class TitlesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title','author', 'release', 'title_urls')
    search_fields = ('title', 'author')
    list_filter = ('release',)
    empty_value_display = '-пусто-'


admin.site.register(Titles, TitlesAdmin)
admin.site.register(Genres)
admin.site.register(Categories)