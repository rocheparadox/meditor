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

def add_pill(request):
    add_pill_template = get_template('add_pill.html')
    return HttpResponse(add_pill_template.render())

def change_pill(request):
    change_pill_template = get_template('change_pill.html')
    return HttpResponse(change_pill_template.render())

def pill_to_patients(request):
    pill_to_patients_template = get_template('pill_to_patients.html')
    return HttpResponse(pill_to_patients_template.render())

def update_slot(request):
    update_slot_template = get_template('update_slot.html')
    return HttpResponse(update_slot_template.render())

def index(request):
    return HttpResponse.write("Util Index")