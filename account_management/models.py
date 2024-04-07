from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image', default='placeholder')
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=11, unique=True)

class PetProfile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=50)
    pet_picture = CloudinaryField('image', default='placeholder')
    breed = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    # vaccination_certificate = CloudinaryField('file', default='placeholder')
    vet_name = models.CharField(max_length=50)
    vet_address_line_1 = models.CharField(max_length=50)
    vet_address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=11)
    