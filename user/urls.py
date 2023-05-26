from django.urls import path, include
from rest_framework import routers

from .views import RegisterAPIView, UserAPIView, LoginAPIView, AdminUserAPIView, AdressAPIView, AdminLoginAPIView


router = routers.DefaultRouter()
router.register(r'users', AdminUserAPIView, basename='users')
router.register(r'user', UserAPIView, basename='user')
router.register(r'adress', AdressAPIView, basename='adress')

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('admin_login/', AdminLoginAPIView.as_view()),
    path('', include(router.urls)),
]
