from django.contrib import admin
from django.urls import path, include
from . import views, api

urlpatterns = [

    #meditor - dev defined urls
    path('/add_patient', views.add_patient),
    path('/change_patient', views.change_patient),
    path('/patients_details', views.patients_details),
    path('/add_pill', views.add_pill),
    path('/change_pill', views.change_pill),
    path('/update_slot', views.update_slot),
    path('/pill_to_patients', views.pill_to_patients),

    #apis
    path('/api/add_patient', api.add_patient),
    path('/api/get_all_patients_details', api.get_all_patients_details),
    path('/api/get_patient_details', api.get_patient_details),
    path('/api/edit_patient', api.edit_patient_details),
    path('/api/add_pill', api.add_pill),
    path('/api/get_all_pills_details', api.get_all_pills_details),
    path('/api/get_all_slot_details', api.get_all_slot_details),
    path('/api/add_pill_to_patient', api.add_pill_to_patient), 
    path('/api/get_pill_details', api.get_pill_details),
    path('/api/update_slot_details', api.update_slot_details),
    path('/api/change_pill', api.change_pill_details)
]