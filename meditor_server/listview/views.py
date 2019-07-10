from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.

def listview_index(request):

    index_template = get_template('base_listview.html')

    return HttpResponse(index_template.render())

