from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register(r'models', ModelAPIView, basename='models')
router.register(r'series', SeriesAPIView, basename='series')
router.register(r'position', PositionAPIView, basename='position')
router.register(r'fuel_sort', FuelSortAPIView, basename='fuel_sort')
router.register(r'gear_box', GearBoxAPIView, basename='gear_box')
router.register(r'garant', GarantAPIView, basename='garant')
router.register(r'branch', BranchAPIView, basename='branch')
router.register(r'images', ImageAPIView, basename='images')
router.register(r'cars', CarAPIView, basename='cars')
router.register(r'defect', DefectAPIView, basename='defect')
router.register(r'defect_images', DefectImageAPIView, basename='defect_image')
router.register(r'comment', CommentAPIView, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]