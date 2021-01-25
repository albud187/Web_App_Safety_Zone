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

from app_reports.models import (
FlightSafetyReport
)

from .serializers import (
FlightSafetyReportSerializer
)

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
        return(response)
