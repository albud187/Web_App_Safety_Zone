from rest_framework import serializers
from app_reports.models import FlightSafetyReport

class FlightSafetyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightSafetyReport
        fields = '__all__'
