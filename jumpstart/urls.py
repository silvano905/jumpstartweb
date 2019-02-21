from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
app_name = 'jumpstart'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('car-not-starting/', views.car_not_starting, name='car-not-starting'),
    path('dead-car-battery/', views.dead_battery, name='dead-car-battery'),

]