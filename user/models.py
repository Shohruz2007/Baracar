import string
import random

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='Users', null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=13, unique=True)
    birthday = models.DateField(null=True, blank=True)
    passport_series = models.CharField(max_length=3, null=True, blank=True)
    passport_number = models.IntegerField(null=True, blank=True)
    verify_code = models.IntegerField(null=True, blank=True)

    ordering = ('phone',)


    USERNAME_FIELD = "phone"

    @property
    def generate_code(self):
        total = string.digits
        verify_code = "".join(random.sample(total, 6))
        self.verify_code = verify_code
        self.save()

    def __str__(self):
        return self.username



class Adress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    country = models.CharField(max_length=55)
    region = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    district = models.CharField(max_length=55, null=True, blank=True)
    street = models.CharField(max_length=55)