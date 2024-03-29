from django.urls import path
from .views import UserProfile

urlpatterns = [
    path('user_profile/', UserProfile.as_view(), name='user_profile'),
]
