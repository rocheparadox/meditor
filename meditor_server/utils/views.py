from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.

def add_patient(request):
    add_patient_template = get_template('add_patient.html')
    return HttpResponse(add_patient_template.render())

def change_patient(request):
    add_patient_template = get_template('change_patient_details.html')
    return HttpResponse(add_patient_template.render())

def patients_details(request):
    patients_details_template = get_template('patients_details.html')
    return HttpResponse(patients_details_template.render())

def index(request):
    return HttpResponse.write("Util Index")