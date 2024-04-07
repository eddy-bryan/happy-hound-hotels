from . import views
from django.urls import path

urlpatterns = [
    path('booking_success/', views.booking_success, name='booking_success'),
    path('', views.home, name='home'),
    path('<slug:slug>/', views.kennel_detail, name='kennel_detail'),
    path('book/<int:kennel_id>/', views.book_now, name='book_now'),
]