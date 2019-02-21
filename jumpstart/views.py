from django.shortcuts import render


def home_view(request):
    return render(request, 'jumpstart/home.html')


def dead_battery(request):
    return render(request, 'jumpstart/dead-car-battery.html')


def car_not_starting(request):
    return render(request, 'jumpstart/car-not-starting.html')