from io import StringIO, BytesIO
from django.db import models

import zipfile
from PIL import Image

from user.models import CustomUser


class CarModel(models.Model):
    name_uz = models.CharField(max_length=55)
    name_ru = models.CharField(max_length=55)
    
    def __str__(self):
        return self.name_uz, self.name_ru


class CarSeries(models.Model):
    name_uz = models.CharField(max_length=55)
    name_ru = models.CharField(max_length=55)
    model = models.ForeignKey(
        CarModel, on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name_uz, self.name_ru


class CarPosition(models.Model):
    name_uz = models.CharField(max_length=55)
    name_ru = models.CharField(max_length=55)
    series = models.ForeignKey(
        CarSeries, on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name_uz, self.name_ru


class CarFuelSort(models.Model):
    name_uz = models.CharField(max_length=55)
    name_ru = models.CharField(max_length=55)

    def __str__(self):
        return self.name_uz, self.name_ru


class CarGearbox(models.Model):
    name_uz = models.CharField(max_length=55)
    name_ru = models.CharField(max_length=55)

    def __str__(self):
        return self.name_uz, self.name_ru


class CarEnginePlace(models.Model):
    name_uz = models.CharField(max_length=55)
    name_ru = models.CharField(max_length=55)

    def __str__(self):
        return self.name_uz, self.name_ru


class CarGarantType(models.Model):
    name_uz = models.CharField(max_length=55)
    name_ru = models.CharField(max_length=55)
    time = models.IntegerField()

    def __str__(self):
        return self.name_uz, self.name_ru


class Branch(models.Model):
    name_uz = models.CharField(max_length=55)
    name_ru = models.CharField(max_length=55)
    
    country_uz = models.CharField(max_length=55)
    country_ru = models.CharField(max_length=55)
    
    region_uz = models.CharField(max_length=55)
    region_ru = models.CharField(max_length=55)
    
    city_uz = models.CharField(max_length=55)
    city_ru = models.CharField(max_length=55)
    
    district_uz = models.CharField(max_length=55, null=True, blank=True)
    district_ru = models.CharField(max_length=55, null=True, blank=True)
    
    street_uz = models.CharField(max_length=55)
    street_ru = models.CharField(max_length=55)

    def __str__(self):
        return self.name_uz, self.name_ru


class Car(models.Model):
    name_uz = models.CharField(max_length=55)
    name_ru = models.CharField(max_length=55)
    
    position = models.ForeignKey(CarPosition, on_delete=models.CASCADE)
    initial_price = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    sale = models.FloatField(default=0)  # 0% = no sale
    depozit = models.FloatField(null=True, blank=True)  # 0 = no depozit
    fuel_consumption = models.FloatField()
    fuel_sort = models.ForeignKey(
        CarFuelSort, on_delete=models.SET_NULL, null=True, blank=True
    )
    year = models.IntegerField()
    distance = models.FloatField(default=0)  # 0 = new car
    gearbox = models.ForeignKey(
        CarGearbox, on_delete=models.SET_NULL, null=True, blank=True
    )
    engine = models.FloatField()
    
    colour_uz = models.CharField(max_length=25)
    colour_ru = models.CharField(max_length=25)
    
    garant = models.ForeignKey(
        CarGarantType, on_delete=models.SET_NULL, null=True, blank=True
    )
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    views = models.IntegerField(default=0)
    
    description_uz = models.TextField()
    description_ru = models.TextField()
    
    time_create = models.DateTimeField(
        auto_now_add=True, null=True
    )  # time when car has created
    time_update = models.DateTimeField(auto_now=True)  # time when car has updated
    is_active = models.BooleanField(default=True)  # car is on sale or not
    engine_power = models.FloatField(null=True, blank=True)
    engine_place = models.ForeignKey(
        CarEnginePlace, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name_uz, self.name_ru


class CarImages(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="CarsImages", unique=True)
    image_file = models.FileField(upload_to="CarImages", null=True, blank=True)



class CarDefect(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to="CarDefectImages")
    image2 = models.ImageField(upload_to="CarDefectImages")
    description_uz = models.TextField()
    description_ru = models.TextField()


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    visit_time = models.DateField()
    is_active = models.BooleanField(default=False)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    description_uz = models.TextField()
    description_ru = models.TextField()


class CarHistory(models.Model):
    name_uz = models.CharField(max_length=55)
    name_ru = models.CharField(max_length=55)
    
    position = models.ForeignKey(CarPosition, on_delete=models.CASCADE)
    initial_price = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    sale = models.FloatField(default=0)  # 0% = no sale
    depozit = models.FloatField(null=True, blank=True)  # 0 = no depozit
    fuel_consumption = models.FloatField()  #
    fuel_sort = models.ForeignKey(
        CarFuelSort, on_delete=models.SET_NULL, null=True, blank=True
    )
    year = models.IntegerField()
    distance = models.FloatField(default=0)  # 0 = new car
    gearbox = models.ForeignKey(
        CarGearbox, on_delete=models.SET_NULL, null=True, blank=True
    )
    engine = models.FloatField()
    engine_power = models.FloatField(null=True, blank=True)
    
    colour_uz = models.CharField(max_length=25)
    colour_ru = models.CharField(max_length=25)
    
    garant = models.ForeignKey(
        CarGarantType, on_delete=models.SET_NULL, null=True, blank=True
    )
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    views = models.IntegerField(default=0)
    
    description_uz = models.TextField()
    description_ru = models.TextField()
    
    time_create = models.DateTimeField(
        auto_now_add=True, null=True
    )  # time when car has created
    time_update = models.DateTimeField(auto_now=True)  # time when car has updated


class Blank(models.Model):
    title = models.CharField(max_length=155)
    text = models.TextField()
    time_field = models.TimeField(auto_now_add=True)