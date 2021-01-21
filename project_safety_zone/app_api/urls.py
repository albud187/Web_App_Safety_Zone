from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register('Flight_Safety_Reports',views.FlightSafetyReportViewSet, basename='Flight_Safety_Reports')

urlpatterns = router.urls
