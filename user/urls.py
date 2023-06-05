from django.urls import path, include
from rest_framework import routers

from .views import RegisterAPIView, UserAPIView, LoginAPIView, AdressAPIView, ChangePasswordView


router = routers.DefaultRouter()
router.register(r'users', UserAPIView, basename='user')
router.register(r'adress', AdressAPIView, basename='adress')

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('', include(router.urls)),
]