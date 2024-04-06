from django.db import models
from django.contrib.auth.models import User
from account_management.models import PetProfile
from datetime import date
from cloudinary.models import CloudinaryField

class Kennel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    kennel_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(max_length=400)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=11, unique=True)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    spaces = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    pet_name = models.ManyToManyField(PetProfile)
    kennel = models.ForeignKey(Kennel, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()


    def is_space_available(self):
        """
        Check if space is available for booking in the kennel between the specified dates.
        """
        # Calculate available spaces for the kennel between check-in and check-out dates
        bookings_within_dates = Booking.objects.filter(
            kennel=self.kennel,
            check_in_date__lte=self.check_out_date,
            check_out_date__gte=self.check_in_date
        )
        booked_spaces = sum(booking.pet_name.count() for booking in bookings_within_dates)
        return self.kennel.spaces - booked_spaces >= self.pet_name.count()


    def is_valid_dates(self):
        """
        Check if the booking dates are valid and not in the past.
        """
        return self.check_in_date > date.today() and self.check_out_date > self.check_in_date


    def save(self, *args, **kwargs):
        """
        Override the save method to validate booking dates and available spaces.
        """
        if self.is_valid_dates() and self.is_space_available():
            super().save(*args, **kwargs)
        else:
            # Raise validation error if dates are invalid or no space is available
            if not self.is_valid_dates():
                raise ValueError("Booking dates must be valid and not in the past")
            elif not self.is_space_available():
                raise ValueError("No space available for booking within the specified dates")