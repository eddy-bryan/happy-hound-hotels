from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
from cloudinary.models import CloudinaryField

class Kennel(models.Model):
    """
    Model representing a kennel.

    Attributes:
        name (str): Name of the kennel.
        slug (str): Slugified version of the kennel name.
        kennel_image (CloudinaryField): Image field for the kennel.
        description (str): Description of the kennel.
        address_line_1 (str): Address line 1 of the kennel.
        address_line_2 (str): Address line 2 of the kennel.
        city (str): City of the kennel.
        county (str): County of the kennel.
        postal_code (str): Postal code of the kennel.
        contact_number (str): Contact number of the kennel.
        price_per_night (Decimal): Price per night of the kennel.
        spaces (int): Number of available spaces in the kennel.
    """

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


    def __str__(self):
        """
        Return string representation of the kennel.
        """
        return f"{self.name} with {self.spaces} spaces based in {self.city} for £{self.price_per_night} per night"


    def save(self, *args, **kwargs):
        """
        Override save method to generate slug from name if not provided.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Booking(models.Model):
    """
    Model representing a booking.

    Attributes:
        customer (User): User who made the booking.
        num_pets (int): Number of pets included in the booking.
        kennel (Kennel): Kennel booked for the stay.
        check_in_date (date): Date of check-in.
        check_out_date (date): Date of check-out.
    """

    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    num_pets = models.IntegerField()
    kennel = models.ForeignKey(Kennel, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()


    def __str__(self):
        """
        Return string representation of the booking.
        """
        return f"Booking for {self.customer} for {self.num_pets} from {self.check_in_date} until {self.check_out_date}"


    def is_space_available(self):
        """
        Check if there are available spaces for the booking.
        """
        booked_spaces = Booking.objects.filter(
            kennel=self.kennel,
            check_in_date__lte=self.check_out_date,
            check_out_date__gte=self.check_in_date
        ).count()

        return self.kennel.spaces - booked_spaces >= int(self.num_pets)


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


class Review(models.Model):
    """
    Model representing a review.

    Attributes:
        kennel (Kennel): Kennel being reviewed.
        author (User): Author of the review.
        body (str): Content of the review.
        created_on (datetime): Date and time when the review was created.
    """

    kennel = models.ForeignKey(
        Kennel,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews_author"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        """
        Return string representation of the review.
        """
        return f"Review for {self.kennel} by {self.author}"