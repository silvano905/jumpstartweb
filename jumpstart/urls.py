from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from . import views
app_name = 'jumpstart'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('car-not-starting/', views.car_not_starting, name='car-not-starting'),
    path('dead-car-battery/', views.dead_battery, name='dead-car-battery'),
    path('thankyou/', views.request_services, name='thankyou'),
    path('sitemap.xml', views.site_map, name='sitemap'),
    path('spanish/', views.spanish_jump_start, name='spanish_jump'),

    path('robots.txt', TemplateView.as_view(template_name="jumpstart/robots.txt", content_type="text/plain"),
         name="robots_file")

]