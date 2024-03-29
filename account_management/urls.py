from . import views
from django.urls import path

urlpatterns = [
    path('user_profile/', views.UserProfile.as_view(), name='user_profile'),
]