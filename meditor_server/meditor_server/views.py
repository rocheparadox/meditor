from django.shortcuts import render
from django.http import HttpResponse
from django.template.backends.django import DjangoTemplates
from django.template.loader import get_template

# Create your views here.

def index(request):
    index_template = get_template('index.html')

    return HttpResponse(index_template.render())

