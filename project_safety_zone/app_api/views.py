from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from django.core import mail
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template.loader import render_to_string

from project_safety_zone.settings import codes_content_dict


from app_reports.models import (
FlightSafetyReport
)

from .serializers import (
FlightSafetyReportSerializer
)

def send_notification(response):
    contact_email = response.data['contact_email']
    contact_number = response.data['contact_number']
    date_time = response.data['date_time']
    description = response.data['description']
    location = response.data['location']
    notification_number = response.data['id']

    recipient_email=codes_content_dict['TARGET_EMAIL']
    email_subject = 'FLIGHT SAFETY NOTIFICATION # ' +str(notification_number)

    html_message = render_to_string('app_reports/FlightSafetyNotification.html',
    {'date_time':date_time,
    'location':location,
    'description': description,
    'contact_email':contact_email,
    'contact_number':contact_number
    })
    plain_message = strip_tags(html_message)

    email_message = EmailMessage(
    email_subject,
    html_message,
    settings.EMAIL_HOST_USER,
    [recipient_email]
    )
    email_message.content_subtype ='html'
    email_message.send()
    print(email_subject)

def upload_file(x):
    pass


class FlightSafetyReportViewSet(viewsets.ModelViewSet):

    serializer_class = FlightSafetyReportSerializer
    queryset = FlightSafetyReport.objects.all()

    def create(self, request, *args, **kwargs):
        response = super(FlightSafetyReportViewSet, self).create(request, *args, **kwargs)
        print('test')
        print(response.data)
        print('test complete')
        # tweak function to send email on submit
        # tweak function send image too
        send_notification(response)
        return(response)

    def update(self, request, *args, **kwargs):
        response = super(FlightSafetyReportViewSet, self).create(request, *args, **kwargs)
        print(response.data['contact_number'])
        print(response.data['description'])
        send_notification(response)
        return(response)
