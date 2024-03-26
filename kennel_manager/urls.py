from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.KennelList.as_view(), name='search'),
]