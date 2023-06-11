import traceback

from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from user.serializers import UserSerializer
from .models import *

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

class SeriesSerializer(serializers.ModelSerializer):
    model = ModelSerializer(read_only=True)
    class Meta:
        model = CarSeries
        fields = ['id','name','model']

class SeriesChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSeries
        fields = ['name','model']


class PositionSerializer(serializers.ModelSerializer):
    series = SeriesSerializer(read_only=True)
    class Meta:
        model = CarPosition
        fields = ['id', 'name', 'series']

class PositionChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPosition
        fields = ['name', 'series']



class FuelSortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarFuelSort
        fields = "__all__"

class GearBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarGearbox
        fields = "__all__"

class GarantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarGarantType
        fields = ['id', 'name', 'time']

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImages
        fields = ['id', 'image', 'car', 'image_file']



class CarSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    fuel_sort = FuelSortSerializer()
    gearbox = GearBoxSerializer()
    garant = GarantSerializer()
    branch = BranchSerializer()
    class Meta:
        model = Car
        fields = '__all__'

class CarChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'



class CarHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarHistory
        fields = '__all__'


class DefectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDefect
        fields = '__all__'

class DefectChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDefect
        fields = '__all__'



class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    car = CarSerializer()
    branch = BranchSerializer()
    class Meta:
        model = Order
        fields = '__all__'

class OrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'