from django.contrib import admin
from .models import Kennel, Booking, Review

admin.site.register(Kennel)
admin.site.register(Booking)
admin.site.register(Review)