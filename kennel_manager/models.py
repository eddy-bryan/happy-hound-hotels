from django.db import models
from django.contrib.auth.models import User
from account_management.models import PetProfile
from datetime import date

class Kennel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=400)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=11, unique=True)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    spaces = models.IntegerField()

class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    pet_name = models.ManyToManyField(PetProfile)
    kennel = models.ForeignKey(Kennel, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()