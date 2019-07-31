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

#keys should be in order
def convert_db_data_to_json_array(keys, data):
    json_array_list = []
    for datum in data:
        datum_dict = {}
        for i in range(len(keys)):
            datum_dict[keys[i]] = datum[i]
        #print(datum_dict)
        json_array_list.append(datum_dict)

    json_dict={}
    json_dict["response"] = json_array_list
    #print(json_dict)
    json_array = json.dumps(json_dict)
    #print(json_array)
    return json_array

def convert_db_data_to_json_obj(keys, data):

    datum = data[0]
    datum_dict = {}
    for i in range(len(keys)):
        datum_dict[keys[i]] = datum[i]
    #print(datum_dict)

    json_array = json.dumps(datum_dict)
    #print(json_array)
    return json_array



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
        db.roll_back()
    return HttpResponse(response)

@csrf_exempt
def edit_patient_details(request):

    response="Error Occured!"
    try:
        print("edit patient api")
        data = request.body.decode('utf-8')
        input_data = parse_data(data)
        print(input_data)

        first_name = input_data.get('first_name')
        last_name = input_data.get('last_name')
        age = input_data.get('age')
        gender = input_data.get('gender')
        email = input_data.get('email')
        patient_id = str(input_data.get('patient_id'))


        db.change_patient_details(first_name, last_name, age, gender, email, patient_id)
        response = "Patient Details edited successfully"

    except Exception as exception:
        print("Error while editing patient " + str(exception))
        db.roll_back()
    return HttpResponse(response)



@csrf_exempt
def get_all_patients_details(request):
    response = "patients data"
    patients_details = db.get_patients_details(-1)
    keys = ["patient_id", "first_name", "last_name", "gender", "email", "age"]
    patients_details_json = convert_db_data_to_json_array(keys, patients_details)
    return HttpResponse(patients_details_json)

@csrf_exempt
def get_patient_details(request):
    print("get patient api")
    data = request.body.decode('utf-8')
    input_data = parse_data(data)
    print(input_data)
    patient_id = input_data.get("patient_id")
    patient_details=db.get_patients_details(patient_id)
    keys = ["patient_id", "first_name", "last_name", "gender", "email", "age"]
    patient_details_json = convert_db_data_to_json_obj(keys, patient_details)
    print(patient_details_json)
    return HttpResponse(patient_details_json)


