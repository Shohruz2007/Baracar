from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router_uz = DefaultRouter()

router_uz.register(r"models", UzModelAPIView, basename="uz/models")
router_uz.register(r"series_get", UzSeriesAPIView, basename="uz/series_get")
router_uz.register(r"position_get", UzPositionAPIView, basename="uz/position_get")
router_uz.register(r"fuel_sort", UzFuelSortAPIView, basename="uz/fuel_sort")
router_uz.register(r"gear_box", UzGearBoxAPIView, basename="uz/gear_box")
router_uz.register(r"garant", UzGarantAPIView, basename="uz/garant")
router_uz.register(r"engine_place", UzEnginePlaceAPIView, basename="uz/engine_place")
router_uz.register(r"branch", UzBranchAPIView, basename="uz/branch")
router_uz.register(r"order_get", UzOrderAPIView, basename="uz/order_get")
router_uz.register(r"cars_get", UzCarAPIView, basename="uz/cars_get")
router_uz.register(r"defect_get", UzDefectAPIView, basename="uz/defect_get")


router_ru = DefaultRouter()

router_ru.register(r"models",RuModelAPIView, basename="ru/models")
router_ru.register(r"series_get", RuSeriesAPIView, basename="ru/series_get")
router_ru.register(r"position_get", RuPositionAPIView, basename="ru/position_get")
router_ru.register(r"fuel_sort", RuFuelSortAPIView, basename="ru/fuel_sort")
router_ru.register(r"gear_box", RuGearBoxAPIView, basename="ru/gear_box")
router_ru.register(r"garant", RuGarantAPIView, basename="ru/garant")
router_ru.register(r"engine_place", RuEnginePlaceAPIView, basename="ru/engine_place")
router_ru.register(r"branch", RuBranchAPIView, basename="ru/branch")
router_ru.register(r"order_get", RuOrderAPIView, basename="ru/order_get")
router_ru.register(r"cars_get", RuCarAPIView, basename="ru/cars_get")
router_ru.register(r"defect_get", RuDefectAPIView, basename="ru/defect_get")


router_no_langual = DefaultRouter()

router_no_langual.register(r"models", ModelChangeAPIView, basename="models")
router_no_langual.register(r"series", SeriesChangeAPIView, basename="series")
router_no_langual.register(r"position", PositionChangeAPIView, basename="position")
router_no_langual.register(r"order", OrderChangeAPIView, basename="order")
router_no_langual.register(r"fuel_sort", FuelSortChangeAPIView, basename="fuel_sort")
router_no_langual.register(r"gear_box", GearBoxChangeAPIView, basename="gear_box")
router_no_langual.register(r"garant", GarantChangeAPIView, basename="garant")
router_no_langual.register(r"branch", BranchChangeAPIView, basename="branch")
router_no_langual.register(r"engine_place", EnginePlaceChangeAPIView, basename="engine_place")
router_no_langual.register(r"images", ImageAPIView, basename="images")
router_no_langual.register(r"cars", CarChangeAPIView, basename="cars")
router_no_langual.register(r"car_history", CarHistoryAPIView, basename="car_history")
router_no_langual.register(r"defect", DefectChangeAPIView, basename="defect")
router_no_langual.register(r"comment", CommentAPIView, basename="comment")
router_no_langual.register(r"blank", BlankAPIView, basename="blank")

urlpatterns = [
    path("", include(router_no_langual.urls)),
    path("uz/", include(router_uz.urls)),
    path("ru/", include(router_ru.urls)),
]
