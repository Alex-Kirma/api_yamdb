from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import (
    TitlesViewSet,
    GenresViewSet,
    CategoriesViewSet
)

router = DefaultRouter()
router.register('titles', TitlesViewSet)
router.register('genres', GenresViewSet)
router.register('categories', CategoriesViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
]
