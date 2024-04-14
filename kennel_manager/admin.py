from django.contrib import admin
from .models import Kennel, Booking, Review

# Register Kennel, Booking, and Review models in the admin panel
admin.site.register(Kennel)
admin.site.register(Booking)
admin.site.register(Review)
