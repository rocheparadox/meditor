#Author : Roche Christopher
#File created on 17 Jul 2019 8:52 AM

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
import json

from DBUtils import db_utils

db=db_utils.DB_UTILS("postgres", "postgres", "localhost", 5432, "meditor")


def parse_data(data):
        print("parse data   -----  " + str(data))
        input_data = json.loads(data).get('input_data')
        return input_data

# Create your views here.

@csrf_exempt
def add_patient(request):

    response="Error Occured!"
    try:
        print("add patient api")
        data = request.body.decode('utf-8')
        input_data = parse_data(data)
        print(input_data)

        first_name = input_data.get('first_name')
        last_name = input_data.get('last_name')
        age = input_data.get('age')
        gender = input_data.get('gender')
        email = input_data.get('email')


        db.add_patient_details(first_name, last_name, age, gender, email)
        response = "Patient Details added successfully"

    except Exception as exception:
        print(exception)
    return HttpResponse(response)