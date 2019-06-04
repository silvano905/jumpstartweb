from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home_view(request):
    return render(request, 'jumpstart/home.html')


def dead_battery(request):
    return render(request, 'jumpstart/dead-car-battery.html')


def spanish_jump_start(request):
    return render(request, 'jumpstart/spanish_jump.html')


def car_not_starting(request):
    return render(request, 'jumpstart/car-not-starting.html')


def site_map(request):
    return render(request, 'jumpstart/sitemap.xml', content_type='text/xml')



def request_services(request):
    get_manual_address = request.POST.get('manual_address')
    phone_number = request.POST.get('phone')
    lengua = request.POST.get('lengua')

    direccion = get_manual_address
    phone_number = ' Phone Number: {}'.format(str(phone_number))
    msg = direccion + phone_number + " : {}".format(lengua)

    email_user = 'silvanovaldez90@yahoo.com'

    send_mail('jumpstartcarservice', 'Bienvenido!', settings.EMAIL_HOST_USER, [email_user], html_message=msg,
              fail_silently=False)
    return render(request, 'jumpstart/thankyou.html', {'lan': 'english', 'total': '60'})
