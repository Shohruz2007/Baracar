from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register(r'models', ModelAPIView, basename='models')
router.register(r'series_get', SeriesAPIView, basename='series')
router.register(r'series', SeriesChangeAPIView, basename='series')
router.register(r'position_get', PositionAPIView, basename='position')
router.register(r'position', PositionChangeAPIView, basename='position')
router.register(r'fuel_sort', FuelSortAPIView, basename='fuel_sort')
router.register(r'gear_box', GearBoxAPIView, basename='gear_box')
router.register(r'garant', GarantAPIView, basename='garant')
router.register(r'engine_place', EnginePlaceAPIView, basename='engine_place')
router.register(r'branch', BranchAPIView, basename='branch')
router.register(r'images', ImageAPIView, basename='images')
router.register(r'cars_get', CarAPIView, basename='cars')
router.register(r'cars', CarChangeAPIView, basename='cars')
router.register(r'car_history', CarHistoryAPIView, basename='car_history')
router.register(r'defect_get', DefectAPIView, basename='defect')
router.register(r'defect', DefectChangeAPIView, basename='defect')
router.register(r'comment', CommentAPIView, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]