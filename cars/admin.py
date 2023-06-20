from django.contrib import admin
from .models import *


class CarPositionAdmin(admin.TabularInline):
    model = CarPosition
    fields = ("name_uz", "name_ru")
    extra = 0


class CarSeriesAdmin(admin.TabularInline):
    model = CarSeries
    fields = ("name_uz", "name_ru")
    extra = 0


class SeriesPositionAdmin(admin.ModelAdmin):
    inlines = [
        CarPositionAdmin
    ]

class ModelSeriesAdmin(admin.ModelAdmin):
    inlines = [
        CarSeriesAdmin
    ]



admin.site.register(Car)
admin.site.register(CarHistory)
admin.site.register(CarSeries, SeriesPositionAdmin)
admin.site.register(CarPosition)
admin.site.register(CarModel, ModelSeriesAdmin)
admin.site.register(CarFuelSort)
admin.site.register(CarGearbox)
admin.site.register(CarGarantType)
admin.site.register(CarEnginePlace)
admin.site.register(Branch)
admin.site.register(CarImages)
admin.site.register(CarDefect)
admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(Blank)
