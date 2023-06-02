from django.db import models

from user.models import CustomUser


class CarModel(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

class CarSeries(models.Model):
    name = models.CharField(max_length=55)
    model = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class CarPosition(models.Model):
    name = models.CharField(max_length=55)
    series = models.ForeignKey(CarSeries, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class CarFuelSort(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

class CarGearbox(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

class CarGarantType(models.Model):
    name = models.CharField(max_length=55)
    time = models.IntegerField()

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=55)
    country = models.CharField(max_length=55)
    region = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    district = models.CharField(max_length=55, null=True, blank=True)
    street = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=55)
    position = models.ForeignKey(CarPosition, on_delete=models.CASCADE)
    initial_price = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    sale = models.FloatField(default=0)  # 0% = no sale
    depozit = models.FloatField(null=True, blank=True)  # 0 = no depozit
    fuel_consumption = models.FloatField()  #
    fuel_sort = models.ForeignKey(CarFuelSort, on_delete=models.SET_NULL, null=True, blank=True)
    year = models.IntegerField()
    distance = models.FloatField(default=0)  # 0 = new car
    gearbox = models.ForeignKey(CarGearbox, on_delete=models.SET_NULL, null=True, blank=True)
    engine = models.FloatField()
    colour = models.CharField(max_length=25)
    garant = models.ForeignKey(CarGarantType, on_delete=models.SET_NULL, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    views = models.IntegerField(default=0)
    description = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True, null=True)  # time when car has created
    time_update = models.DateTimeField(auto_now=True)  # time when car has updated
    is_active = models.BooleanField(default=True)  # car is on sale or not

    def __str__(self):
        return self.name

class CarImages(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="CarImages")

class CarDefectImages(models.Model):
    image = models.ImageField(upload_to="CarImages")


class CarDefect(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ManyToManyField(CarDefectImages)
    description = models.TextField(null=True)

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


