from django.shortcuts import render
from django.http import HttpResponse
from django.template.backends.django import DjangoTemplates
from django.template.loader import get_template

# Create your views here.

def nurse_portal(request):
    nurse_portal_template = get_template('nurse_portal.html')
    return HttpResponse(nurse_portal_template.render())

def doctor_portal(request):
    nurse_portal_template = get_template('doctor_portal.html')
    return HttpResponse(nurse_portal_template.render())

def patient_portal(request):
    nurse_portal_template = get_template('patient_portal.html')
    return HttpResponse(nurse_portal_template.render())
