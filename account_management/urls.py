from django.urls import path
from . import views

urlpatterns = [
    path('user_profile', views.user_profile, name='user_profile'),
    path('<str:owner>/<str:pet_name>/', views.pet_profile, name='pet_profile'),
]
