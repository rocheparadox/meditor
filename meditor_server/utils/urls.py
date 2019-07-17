from django.contrib import admin
from django.urls import path, include
from . import views, api

urlpatterns = [

    #meditor - dev defined urls
    path('/add_patient', views.add_patient),

    #apis
    path('/api/add_patient', api.add_patient)
]