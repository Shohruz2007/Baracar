import traceback

from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from user.serializers import UserSerializer
from .models import *


class UzModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id','name_uz']

class RuModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id','name_ru']

class ModelChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class UzSeriesSerializer(serializers.ModelSerializer):
    model = UzModelSerializer(read_only=True)

    class Meta:
        model = CarSeries
        fields = ['id','name_uz', 'model']
        
class RuSeriesSerializer(serializers.ModelSerializer):
    model = RuModelSerializer(read_only=True)

    class Meta:
        model = CarSeries
        fields = ['id','name_ru', 'model']


class SeriesChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSeries
        fields = "__all__"


class UzPositionSerializer(serializers.ModelSerializer):
    series = UzSeriesSerializer(read_only=True)

    class Meta:
        model = CarPosition
        fields = ['id','name_uz', 'series']

class RuPositionSerializer(serializers.ModelSerializer):
    series = RuSeriesSerializer(read_only=True)

    class Meta:
        model = CarPosition
        fields = ['id','name_ru', 'series']


class PositionChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPosition
        fields = "__all__"


class UzFuelSortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarFuelSort
        fields = ['id','name_uz']

class RuFuelSortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarFuelSort
        fields = ['id','name_ru']

class FuelSortChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarFuelSort
        fields = '__all__'


class UzGearBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarGearbox
        fields = ['id','name_uz']

class RuGearBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarGearbox
        fields = ['id','name_ru']

class GearBoxChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarGearbox
        fields = '__all__'


class UzGarantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarGarantType
        fields = ['id','name_uz', 'time']

class RuGarantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarGarantType
        fields = ['id','name_ru', 'time']

class GarantChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarGarantType
        fields = '__all__'


class UzBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['name_uz', 'country_uz', 'region_uz', 'city_uz', 'district_uz', 'street_uz']

class RuBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['name_ru', 'country_ru', 'region_ru', 'city_ru', 'district_ru', 'street_ru']

class BranchChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class UzEnginePlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarEnginePlace
        fields = ['id','name_uz']

class RuEnginePlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarEnginePlace
        fields = ['id','name_ru']

class EnginePlaceChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarEnginePlace
        fields = '__all__'


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImages
        fields = "__all__"


class UzCarSerializer(serializers.ModelSerializer):
    position = UzPositionSerializer()
    fuel_sort = UzFuelSortSerializer()
    gearbox = UzGearBoxSerializer()
    garant = UzGarantSerializer()
    branch = UzBranchSerializer()
    engine_place = UzEnginePlaceSerializer()

    class Meta:
        model = Car
        fields = ['name_uz','position','initial_price','price','sale','depozit','fuel_consumption','fuel_sort','year','distance','gearbox','engine','colour_uz','garant','branch','views','description_uz','time_create','time_update','is_active','engine_power','engine_place']

class RuCarSerializer(serializers.ModelSerializer):
    position = RuPositionSerializer()
    fuel_sort = RuFuelSortSerializer()
    gearbox = RuGearBoxSerializer()
    garant = RuGarantSerializer()
    branch = RuBranchSerializer()
    engine_place = RuEnginePlaceSerializer()

    class Meta:
        model = Car
        fields = ['name_ru','position','initial_price','price','sale','depozit','fuel_consumption','fuel_sort','year','distance','gearbox','engine','colour_ru','garant','branch','views','description_ru','time_create','time_update','is_active','engine_power','engine_place']


class CarChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarHistory
        fields = "__all__"


class UzDefectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDefect
        fields = ['car','image1','image2','description_uz']

class RuDefectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDefect
        fields = ['car','image1','image2','description_ru']


class DefectChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDefect
        fields = "__all__"


class UzOrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    car = UzCarSerializer()
    branch = UzBranchSerializer()

    class Meta:
        model = Order
        fields = "__all__"

class RuOrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    car = RuCarSerializer()
    branch = RuBranchSerializer()

    class Meta:
        model = Order
        fields = "__all__"


class OrderChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class BlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blank
        fields = "__all__"
