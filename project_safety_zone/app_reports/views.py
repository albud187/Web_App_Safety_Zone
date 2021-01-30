from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class FlightSafetyReportView(TemplateView):
    template_name = 'app_reports/FlightSafetyReportForm.html'

class FlightSafetyReportConfirmView(TemplateView):
    template_name = 'app_reports/FlightSafetyReportConfirm.html'
