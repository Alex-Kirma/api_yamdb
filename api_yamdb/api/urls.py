from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
#from api.views import APISignUp,
from api.views import SignUp, APIToken, UsersViewSet, UsernameViewSet
from rest_framework import viewsets

router = DefaultRouter()

app_name = 'api'
router.register('auth/signup', SignUp, basename='signup')
router.register(r'users/(?P<username>[\w.@+-]+)', UsernameViewSet, basename='users')

router.register('users', UsersViewSet)
#router.register(r'users/(?P<username>^[\w.+-]+/z)', UsernameViewSet, basename='users')


#router.register('auth/token', APIToken.as_view(), basename='token') 
#router.register('auth/token', TokenObtainPairView.as_view()),
#router.register('auth/signup', APISignUp.as_view(), basename='signup')

urlpatterns = [
    #path('v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    #path('v1/auth/signup/', APISignUp.as_view())
    path('v1/auth/token/', APIToken.as_view()),
    path('v1/', include(router.urls)),
]