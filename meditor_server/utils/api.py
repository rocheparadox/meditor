#Author : Roche Christopher
#File created on 17 Jul 2019 8:52 AM

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
import json

from DBUtils import db_utils

db=db_utils.DB_UTILS("postgres", "paragon01", "localhost", 5432, "meditor")


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
    #response = "patients data"
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

@csrf_exempt
def add_pill(request):

    response="Error Occured!"
    try:
        print("add pill api")
        data = request.body.decode('utf-8')
        input_data = parse_data(data)
        print(input_data)

        pill_name = input_data.get('pill_name')

        db.add_pill_details(pill_name)
        response = "Pill Details added successfully"

    except Exception as exception:
        print(exception)
        db.roll_back()
    return HttpResponse(response)

@csrf_exempt
def get_all_pills_details(request):
    #response = "patients data"
    pill_details = db.get_pill_details(-1)
    keys = ["pill_id", "pill_name"]
    pill_details_json = convert_db_data_to_json_array(keys, pill_details)
    return HttpResponse(pill_details_json)

@csrf_exempt
def get_all_slot_details(request):
    #response = "slots data"
    slot_details = db.get_all_slot_details(-1)
    keys = ["slotid", "slotnumber","slotstatus"]
    slot_details_json = convert_db_data_to_json_array(keys, slot_details)
    return HttpResponse(slot_details_json)

@csrf_exempt
def update_slot_details(request):
    response = "Error occurred"
    data = request.body.decode('utf-8')
    input_data = parse_data(data)
    print(input_data)
    slotid = input_data.get('slotid')
    db.change_slot_status(slotid,'open')
    response = "Slot:"+slotid+" released successfully"
    return HttpResponse(response)

@csrf_exempt
def add_pill_to_patient(request):
    response="Error Occured!"
    try:
        print("add pill to patient details")
        data = request.body.decode('utf-8')
        input_data = parse_data(data)
        print(input_data)
        #pill_id = input_data.get('pill_id')
        patient_id = input_data.get('patient_id')
        slotid = input_data.get('slotid')
        scheduledt = input_data.get('scheduledt')
        clock = input_data.get('clock')

        db.change_slot_status(slotid,'close')
        schedule_id=str(db.add_schedule_details(scheduledt, clock,scheduledt))
        schedule_to_slot_detailsid=str(db.add_schedule_to_slot_details(schedule_id, slotid))
        #print(schedule_to_slot_detailsid)
        db.add_patient_schedule_and_slot_details(patient_id, schedule_to_slot_detailsid)
        response = "Pill to Patient Details added successfully"

    except Exception as exception:
        print(exception)
        db.roll_back()
    return HttpResponse(response)

@csrf_exempt
def get_pill_details(request):
    print("Get Pill api")
    data = request.body.decode('utf-8')
    input_data = parse_data(data)
    print(input_data)
    pill_id = input_data.get("pill_id")
    pill_details=db.get_pill_details(pill_id)
    keys = ["pill_id", "pill_name"]
    pill_details_json = convert_db_data_to_json_obj(keys, pill_details)
    print(pill_details_json)
    return HttpResponse(pill_details_json)

@csrf_exempt
def change_pill_details(request):
    response="Error Occured!"
    try:
        print("edit pill api")
        data = request.body.decode('utf-8')
        input_data = parse_data(data)
        print(input_data)

        pill_name = input_data.get('pill_name')
        pill_id = str(input_data.get('pill_id'))


        db.change_pill_details(pill_name, pill_id)
        response = "Pill Details edited successfully"

    except Exception as exception:
        print("Error while editing pill " + str(exception))
        db.roll_back()
    return HttpResponse(response)
