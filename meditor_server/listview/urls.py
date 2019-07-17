from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    #meditor - dev defined urls
    path('', views.listview_index),
    path('patient_listview',views.patient_listview)
]