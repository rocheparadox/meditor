#File created on 11 Jul 2019 8:15 AM

import psycopg2

class DB_UTILS:
    def __init__(self, username, password, hostname, port, databasename):
        self.username = username
        self.password = password
        self.databasename = databasename
        self.hostname = hostname
        self.port = port

        self.conn = psycopg2.connect(host=hostname, port=port, database=databasename, user=username, password=password)

    #Default for insert queries
    def execute_query(self, query):
        print("Going to execute query --- " + query)
        cur = self.conn.cursor()
        # cur.execute('select * from queen')
        cur.execute(query)
        # db_users = cur.fetchone()
        # print(db_users)
        self.conn.commit()
        cur.close()

    #roll back the query
    def roll_back(self):
        self.conn.rollback()

    def get_data_from_database(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()

        return data



    def get_patients_details(self, patient_id=-1):
        if patient_id == -1:
            query = "select * from patientdetails;"
            patient_details = self.get_data_from_database(query)
            print(patient_details)
        else:
            query = "select * from patientdetails where patientid=" + patient_id
            patient_details = self.get_data_from_database(query)
            print(patient_details)

        return patient_details

    #fetch all patients data

    def add_patient_details(self, first_name, last_name, age, gender, email):
        query = "insert into patientdetails(firstname, lastname, age, gender, email) values('"+first_name+"','"+last_name+"','"+age+"','"+gender+"','"+email+"')"
        self.execute_query(query)


    def add_pill_details(self, pill_name):
        query = "insert into tabletdetails(tabletname) values('" + pill_name + "')"
        self.execute_query(query)

    def add_bed_details(self, bed_number):
        query = "insert into beddetails(bednumber) values('" + bed_number + "')"
        self.execute_query(query)

    def change_patient_details(self, first_name, last_name, age, gender, email, patient_id):
        query = "update patientdetails set " \
                "firstname='"+first_name+"', " \
                "lastname='"+last_name+"', " \
                "age='"+age+"', " \
                "gender='"+gender+"', " \
                "email='"+email+"' " \
                "where patientid=" + patient_id
        self.execute_query(query)

    def change_pill_details(self, pill_name, pill_id):
        query = "update tabletdetails set tablename='" + pill_name +"' where tabletid=" + pill_id
        self.execute_query(query)




    def add_doctor_details(self, first_name, last_name, email):
        query= "insert into doctordetails(firstname, lastname, email) value('"+first_name+"','"+last_name+"','"+email+"')"
        self.execute_query(query)

    def change_doctor_details(self, first_name, last_name, email, doctor_id):
        query = "update dotordetails set " \
                "firstname='"+first_name+"', " \
                "lastname='"+last_name+"', " \
                "email='"+email+"' " \
                "where doctorid=" + doctor_id
        self.execute_query(query)

    def add_doctor_to_patient_details(self, patient_id, doctor_id):
        query= "insert into doctortopatientdetails(patientid, doctorid) value('"+patient_id+"','"+doctor_id+"')"
        self.execute_query(query)

    def change_doctor_to_patient_details(self, patient_id, doctor_id, doctor_to_patient_details_id):
        query = "update doctortopatientdetails set " \
                "patientid='"+patient_id+"', " \
                "doctorid='"+doctor_id+"',"\
                "where doctortopatientdetailsid=" + doctor_to_patient_details_id
        self.execute_query(query)

    def add_patient_schedule_and_slot_details(self, patient_id, schedule_to_slot_detailsid):
        query= "insert into patientscheduleandslotdetails(patientid, scheduletoslotdetailsid) value('"+patient_id+"','"+schedule_to_slot_detailsid+"')"
        self.execute_query(query)

    def change_patient_schedule_and_slot_details(self, patient_id, schedule_to_slot_details_id, patient_toss_id):
        query = "update patientscheduleandslotdetails set " \
                "patientid='"+patient_id+"', " \
                "scheduletoslotdetailsid='"+schedule_to_slot_details_id+"', " \
                "where patienttossid=" + patient_toss_id
        self.execute_query(query)

    def add_patient_to_bed_details(self, patient_id, bed_id):
        query= "insert into patienttobeddetails(patientid, bedid) value('"+patient_id+"','"+bed_id+"')"
        self.execute_query(query)

    def change_patient_to_bed_details(self, patient_id, bed_id, patient_to_bed_details_id ):
        query= "update patienttobeddetails set" \
               "patientid='"+patient_id+"', " \
               "bedid='"+bed_id+"', " \
               "where patienttobeddetailsid=" + patient_to_bed_details_id
        self.execute_query(query)

    def add_schedule_details(self, day, clock):
        query= "insert into scheduledetails(day, clock) value('"+day+"','"+clock+"')"
        self.execute_query(query)

    def change_schedule_details(self,day, clock, schedule_id):
        query= "update scheduledetails set" \
               "day= '"+day+"', " \
               "clock= '"+clock+"', " \
               "where scheduleid=" + schedule_id
        self.execute_query(query)

    def add_schedule_to_slot_details(self, schedule_id, slot_id):
        query= "insert into scheduletoslotdetails(scheduleid, slotid) value('"+schedule_id+"','"+slot_id+"')"
        self.execute_query(query)

    def change_schedule_to_slot_details(self, schedule_id, slot_id, schedule_to_slot_details_id):
        query= "update scheduletoslotdetails set" \
               "scheduleid= '" +schedule_id+"', " \
               "slotid= '"+slot_id+"', " \
               "where scheduletoslotdetailsid=" + schedule_to_slot_details_id
        self.execute_query(query)

    def add_slot_details(self, slot_number):
        query= "insert into slotdetails(slotnumber) value('"+slot_number+"')"
        self.execute_query(query)

    def change_slot_details(self, slot_number, slot_id):
        query= "update slotdetails set" \
               "slotnumber= '"+slot_number+"', " \
               "where slotid=" + slot_id
        self.execute_query(query)

    def change_bed_details(self, bed_number, bed_id):
        query = "update beddetails set " \
                "bednumber='"+bed_number+"', " \
                "where bedid=" + bed_id
        self.execute_query(query)



