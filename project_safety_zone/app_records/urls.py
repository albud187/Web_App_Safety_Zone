from django.contrib import admin
from django.urls import path, include
from. import views
urlpatterns = [
    path('records/',views.FlightSafetyRecordView.as_view(),name='records'),
]
