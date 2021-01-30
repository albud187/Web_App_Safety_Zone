from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class FlightSafetyRecordView(TemplateView):
    template_name = 'app_records/ReportRecords.html'
