from django.urls import path, include
from rest_framework import routers

from .views import RegisterAPIView, LoginAPIView, UserAPIView, AdressAPIView


router = routers.DefaultRouter()
router.register(r'user', UserAPIView, basename='user')
router.register(r'adress', AdressAPIView, basename='adress')

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('', include(router.urls)),
]
