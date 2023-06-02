from rest_framework import serializers

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

class SeriesPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSeries
        fields = ['name','model']


class PositionSerializer(serializers.ModelSerializer):
    series = SeriesSerializer()
    class Meta:
        model = CarPosition
        fields = ['id','name','series']

class PositionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPosition
        fields = ['name','series']



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
        fields = ['id', 'image', 'car']


class CarSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    fuel_sort = FuelSortSerializer()
    gearbox = GearBoxSerializer()
    garant = GarantSerializer()
    branch = BranchSerializer()
    class Meta:
        model = Car
        fields = '__all__'


class CarHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CarPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'



class DefectImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarDefectImages
        fields = '__all__'

class DefectSerializer(serializers.ModelSerializer):
    image = DefectImageSerializer(many=True)
    class Meta:
        model = CarDefect
        fields = '__all__'

class DefectPostSerializer(serializers.ModelSerializer):
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