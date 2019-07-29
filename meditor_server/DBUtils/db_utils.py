#Author : Roche Christopher
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
        pass



    def get_patients_details(self, patient_id=-1):
        if patient_id == -1:
            query = "select * from "

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
