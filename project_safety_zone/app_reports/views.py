from django.shortcuts import render

# Create your views here.
from django.core import mail
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.views.generic import TemplateView

class FlightSafetyReportView(TemplateView):
    template_name = 'app_reports/FlightSafetyReportForm.html'
