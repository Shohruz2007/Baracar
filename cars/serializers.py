from rest_framework import serializers

from user.serializers import UserSerializer
from .models import *

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

class SeriesSerializer(serializers.ModelSerializer):
    model = ModelSerializer()
    class Meta:
        model = CarSeries
        fields = ['id','name','model']

class PositionSerializer(serializers.ModelSerializer):
    series = SeriesSerializer()
    class Meta:
        model = CarPosition
        fields = ['id','name','series']

class FuelSortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarFuelSort
        fields = ['name']

class GearBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarGearbox
        fields = ['name']

class GarantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarGarantType
        fields = ['name', 'time']

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImages
        fields = ['image']

class CarSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    fuel_sort = FuelSortSerializer()
    gearbox = GearBoxSerializer()
    garant = GarantSerializer()
    branch = BranchSerializer()
    image = CarImageSerializer(many=True)
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

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    car = CarSerializer()
    branch = BranchSerializer()
    class Meta:
        model = Order
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'