from django.contrib import admin
from django.urls import path, include
from. import views

urlpatterns = [
    path('',views.FlightSafetyReportView.as_view(),name='report'),
    path('test',views.test, name='test')
]
