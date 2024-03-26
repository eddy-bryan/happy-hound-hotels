from . import views
from django.urls import path

urlpatterns = [
    path('', views.KennelList.as_view(), name='home'),
]