from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
import json
import requests
from django.contrib import messages

MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
members_endpoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'


# Create your views here.
def index(request):
    if request.method == "POST":
        subject = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']

        contact = 'subject:' + subject + '\n email:' + email + '\n phone:' + phone

        send_mail(
            subject,
            contact,
            email,
            ['familyvibestz@gmail.com'],
            fail_silently=False
        )
        return render(request, 'index.html', {'subject': subject})

    else:
        return render(request, 'index.html', {})

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    if request.method == "POST":
        subject = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']

        contact = 'subject:' + subject + '\n email:' + email + '\n phone:' + phone

        send_mail(
            subject,
            contact,
            email,
            ['familyvibestz@gmail.com'],
            fail_silently=False
        )
        return render(request, 'services.html', {'subject': subject})

    else:
        return render(request, 'services.html', {})

    return render(request, 'services.html')


def photo(request):
    return render(request, 'photo.html')


def video(request):
    return render(request, 'video.html')


def contact(request):
    if request.method == "POST":
        subject = request.POST['name']
        email = request.POST['email']
        message = request.POST.get(str('message'))
        phone = request.POST['phone']

        contact = 'subject:' + subject + '\n email:' + email + '\n message:' + str(message) + '\n phone:' + phone

        send_mail(
            subject,
            contact,
            email,
            ['familyvibestz@gmail.com'],
            fail_silently=False
        )
        return render(request, 'contact.html', {'subject': subject})

    else:
        return render(request, 'contact.html', {})


def booking(request):
    if request.method == "POST":
        Jina_la_Mteja = request.POST.get(str('Jina_la_Mteja'))
        Mahali_anapoishi = request.POST.get(str('Mahali_anapoishi'))
        Jinsia = request.POST.get(str('Jinsia'))
        Namba_ya_simu = request.POST.get(str('Namba_ya_simu'))
        Email = request.POST.get(str('Email'))
        Tarehe = request.POST.get(str('Tarehe'))
        Muda_wa_kukutana = request.POST.get(str('time'))
        Huduma_ninayoitaji = request.POST.get(str('type'))
        Muda_wa_kupata_huduma = request.POST.get(str('time_service'))
        Status = request.POST.get(str('Status'))

        appointment = 'Jina_la_Mteja:' + str(Jina_la_Mteja) + '\n Mahali_anapoishi:' + str(
            Mahali_anapoishi) + '\n insia:' + str(Jinsia) + '\n Namba_ya_simu:' + str(Namba_ya_simu) + '\n Email:' + str(Email) + '\n Tarehe:' + str(Tarehe) + '\n Muda_wa_kukutana:' + str(Muda_wa_kukutana) + '\n Huduma_ninayoitaji:' + str(Huduma_ninayoitaji) + '\n Muda_wa_kupata_huduma:' + str(Muda_wa_kupata_huduma) + '\n Status:' + str(Status)

        send_mail(
            Jina_la_Mteja,
            appointment,
            Email,
            ['familyvibestz@gmail.com'],
            fail_silently=False
        )

        return render(request, 'booking.html', {'Jina_la_Mteja': Jina_la_Mteja})

    else:
        return render(request, 'booking.html', {})
