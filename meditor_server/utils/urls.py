from django.contrib import admin
from django.urls import path, include
from . import views, api

urlpatterns = [

    #meditor - dev defined urls
    path('/add_patient', views.add_patient),
    path('/change_patient', views.change_patient),
    path('/patients_details', views.patients_details),

    #apis
    path('/api/add_patient', api.add_patient),
    path('/api/get_all_patients_details', api.get_all_patients_details),
    path('/api/get_patient_details', api.get_patient_details),
    path('/api/edit_patient', api.edit_patient_details)
]