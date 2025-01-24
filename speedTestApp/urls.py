from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='dashboard'),  # Route to the speed test view
     path('run_speedtest/', views.run_speedtest, name='run_speedtest'),
      path('run_speedtest/', views.run_speedtest, name='run_speedtest'),  # Add this
]