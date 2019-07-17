from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    #meditor - dev defined urls
    path('/nurse_portal', views.nurse_portal),
    path('/doctors_portal', views.doctor_portal),
    path('/patients_portal', views.patient_portal)
]