from rest_framework import serializers
from rest_framework.utils import model_meta

from user.serializers import UserOnlyNameSerializer, UserSerializer
from .models import *


class UzModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55, source='name_uz')
    class Meta:
        model = CarModel
        fields = ['id','name']

class RuModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55, source='name_ru')
    class Meta:
        model = CarModel
        fields = ['id','name']

class ModelChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class UzSeriesSerializer(serializers.ModelSerializer):
    model = UzModelSerializer(read_only=True)
    name = serializers.CharField(max_length=55, source='name_uz')
    class Meta:
        model = CarSeries
        fields = ['id','name', 'model']
        
class RuSeriesSerializer(serializers.ModelSerializer):
    model = RuModelSerializer(read_only=True)
    name = serializers.CharField(max_length=55, source='name_ru')
    class Meta:
        model = CarSeries
        fields = ['id','name', 'model']


class SeriesChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSeries
        fields = "__all__"


class UzPositionSerializer(serializers.ModelSerializer):
    series = UzSeriesSerializer(read_only=True)
    name = serializers.CharField(max_length=55, source='name_uz')
    class Meta:
        model = CarPosition
        fields = ['id','name', 'series']

class RuPositionSerializer(serializers.ModelSerializer):
    series = RuSeriesSerializer(read_only=True)
    name = serializers.CharField(max_length=55, source='name_ru')
    class Meta:
        model = CarPosition
        fields = ['id','name', 'series']


class PositionChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPosition
        fields = "__all__"


class UzFuelSortSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55, source='name_uz')
    class Meta:
        model = CarFuelSort
        fields = ['id','name']

class RuFuelSortSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55, source='name_ru')
    class Meta:
        model = CarFuelSort
        fields = ['id','name']

class FuelSortChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarFuelSort
        fields = '__all__'


class UzGearBoxSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55, source='name_uz')
    class Meta:
        model = CarGearbox
        fields = ['id','name']

class RuGearBoxSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55, source='name_ru')
    class Meta:
        model = CarGearbox
        fields = ['id','name']

class GearBoxChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarGearbox
        fields = '__all__'


class UzGarantSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55, source='name_uz')
    class Meta:
        model = CarGarantType
        fields = ['id','name', 'time']

class RuGarantSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55, source='name_ru')
    class Meta:
        model = CarGarantType
        fields = ['id','name', 'time']

class GarantChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarGarantType
        fields = '__all__'


class UzBranchSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55, source='name_uz')
    country = serializers.CharField(max_length=55, source='country_uz')
    region = serializers.CharField(max_length=55, source='region_uz')
    city = serializers.CharField(max_length=55, source='city_uz')
    district = serializers.CharField(max_length=55, source='district_uz')
    street = serializers.CharField(max_length=55, source='street_uz')
    class Meta:
        model = Branch
        fields = ['id','name', 'country', 'region', 'city', 'district', 'street']

class RuBranchSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55, source='name_ru')
    country = serializers.CharField(max_length=55, source='country_ru')
    region = serializers.CharField(max_length=55, source='region_ru')
    city = serializers.CharField(max_length=55, source='city_ru')
    district = serializers.CharField(max_length=55, source='district_ru')
    street = serializers.CharField(max_length=55, source='street_ru')
    class Meta:
        model = Branch
        fields = ['id','name', 'country', 'region', 'city', 'district', 'street']

class BranchChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class BranchMinInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name_uz', 'name_ru']


class UzEnginePlaceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55, source='name_uz')
    class Meta:
        model = CarEnginePlace
        fields = ['id','name']

class RuEnginePlaceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55, source='name_ru')
    class Meta:
        model = CarEnginePlace
        fields = ['id','name']

class EnginePlaceChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarEnginePlace
        fields = '__all__'


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImages
        fields = "__all__"


class UzCarSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55, source='name_uz')
    description = serializers.CharField(max_length=55, source='description_uz')
    colour = serializers.CharField(max_length=55, source='colour_uz')
    position = UzPositionSerializer()
    fuel_sort = UzFuelSortSerializer()
    gearbox = UzGearBoxSerializer()
    garant = UzGarantSerializer()
    branch = UzBranchSerializer()
    engine_place = UzEnginePlaceSerializer()

    class Meta:
        model = Car
        fields = ['id','name','position','initial_price','price','sale','depozit','fuel_consumption','fuel_sort','year','distance','gearbox','engine','colour','garant','branch','views','description','time_create','time_update','is_active','engine_power','engine_place']

class RuCarSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length=55, source='description_ru')
    name = serializers.CharField(max_length=55, source='name_ru')
    colour = serializers.CharField(max_length=55, source='colour_ru')
    position = RuPositionSerializer()
    fuel_sort = RuFuelSortSerializer()
    gearbox = RuGearBoxSerializer()
    garant = RuGarantSerializer()
    branch = RuBranchSerializer()
    engine_place = RuEnginePlaceSerializer()

    class Meta:
        model = Car
        fields = ['id','name','position','initial_price','price','sale','depozit','fuel_consumption','fuel_sort','year','distance','gearbox','engine','colour','garant','branch','views','description','time_create','time_update','is_active','engine_power','engine_place']


class CarChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

class CarMinInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name_uz', 'name_ru']


class CarHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarHistory
        fields = "__all__"


class UzDefectSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length=55, source='description_uz')
    class Meta:
        model = CarDefect
        fields = ['id','car','image1','image2','description']

class RuDefectSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length=55, source='description_ru')
    class Meta:
        model = CarDefect
        fields = ['id','car','image1','image2','description']


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

class OrderGetSerializer(serializers.ModelSerializer):
    user = UserOnlyNameSerializer()
    car = CarMinInfoSerializer()
    branch = BranchMinInfoSerializer()
    class Meta:
        model = Order
        fields = ['id','user','car','branch','time_create','visit_time','is_active','message']


class CallToUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallToUser
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class BlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blank
        fields = "__all__"
