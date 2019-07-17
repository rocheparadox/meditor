from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.

def add_patient(request):
    add_patient_template = get_template('add_patient.html')
    return HttpResponse(add_patient_template.render())

def index(request):
    return HttpResponse.write("Util Index")