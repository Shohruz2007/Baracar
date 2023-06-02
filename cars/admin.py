from django.contrib import admin
from .models import *

class CarSeriesAdmin(admin.TabularInline):
    model = CarSeries
    fields = ("name",)
    extra = 0


class ModelSeriesAdmin(admin.ModelAdmin):
    inlines = [
        CarSeriesAdmin
    ]

class CarSubcategory(admin.ModelAdmin):
    inlines = [
        CarSeriesAdmin
    ]


admin.site.register(Car)
admin.site.register(CarHistory)
admin.site.register(CarSeries)
admin.site.register(CarPosition)
admin.site.register(CarModel, ModelSeriesAdmin)
admin.site.register(CarFuelSort)
admin.site.register(CarGearbox)
admin.site.register(CarGarantType)
admin.site.register(Branch)
admin.site.register(CarImages)
admin.site.register(CarDefect)
admin.site.register(CarDefectImages)
admin.site.register(Comment)
