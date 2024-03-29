import string
import random

from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='Users', null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=13, unique=True)
    birthday = models.DateField(null=True, blank=True)
    passport_series = models.CharField(max_length=3, null=True, blank=True)
    passport_number = models.IntegerField(null=True, blank=True)
    verify_code = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=150)
    image = models.ImageField(upload_to='UserImages',null=True, blank=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        help_text=_(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )


    ordering = ('phone',)  # phone field is on username field's place

    REQUIRED_FIELDS = ['username']  # for creating superuser
    USERNAME_FIELD = "phone"

    @property
    def generate_code(self):  # generating verify_code by using python random
        total = string.digits
        verify_code = "".join(random.sample(total, 6))
        self.verify_code = verify_code
        self.save()
        return verify_code

    def __str__(self):
        return self.username



class Adress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    country = models.CharField(max_length=55)
    region = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    district = models.CharField(max_length=55, null=True, blank=True)
    street = models.CharField(max_length=55)
