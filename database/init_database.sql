create database meditor;

\c meditor;

create table PatientDetails(
  PATIENTID serial PRIMARY KEY,
  FirstName varchar (50) NOT NULL,
  LastName varchar (50) Not Null,
  Gender varchar (25) check (Gender='Male' OR Gender= 'Female' OR Gender= 'F' OR Gender-= 'M') NOT Null,
  Email varchar (150),
  CountryOfBirth varchar (50) NOT NULL,
  UNIQUE (Email)
);

create table DoctorDetails(
  DOCTORID serial PRIMARY KEY,
  FirstName varchar (50) NOT NULL,
  LastName varchar (50) NOT NULL,
  Email varchar (150),
  UNIQUE (Email)
);

create table TabletDetails(
  TABLETID serial PRIMARY KEY,
  TABLETNAME varchar (50) NOT NULL
);

create table BedDetails(
  BEDID serial PRIMARY KEY,
  BEDNUMBER integer NOT NULL
);

create table SlotDetails(
  SLOTID serial PRIMARY KEY,
  SLOTNUMBER integer NOT NULL
);

create table ScheduleDetails(
  SCHEDULEID serial PRIMARY KEY,
  DAY varchar (10) NOT NULL,
  CLOCK time NOT NULL,
  UNIQUE(DAY, CLOCK)
);

/* Relationship tables*/

create table PatientToBedDetails(
  PATEIENTTOBEDDETAILSID serial PRIMARY KEY,
  PATIENTID integer NOT NULL references PatientDetails(PATIENTID),
  BEDID Integer NOT NULL references BedDetails(BEDID),
  UNIQUE(PATIENTID),
  UNIQUE(BEDID)
);

create table ScheduleToSlotDetails(
  SCHEDULETOSLOTDETAILSID serial PRIMARY KEY,
  SCHEDULEID integer NOT NULL references ScheduleDetails(SCHEDULEID),
  SLOTID Integer NOT NULL references SlotDetails(SLOTID),
  UNIQUE(SCHEDULEID,SLOTID)
);

create table PatientScheduleAndSlotDetails(
  PATIENTTOSSID serial PRIMARY KEY,
  PATIENTID integer NOT NULL references PatientDetails(PATIENTID),
  SCHEDULETOSLOTDETAILSID Integer NOT NULL references ScheduleToSlotDetails(SCHEDULETOSLOTDETAILSID),
  UNIQUE(PATIENTID, SCHEDULETOSLOTDETAILSID)
);

create table DoctorToPatientDetails(
  DOCTORTOPATIENTDETAILSID serial PRIMARY KEY,
  PATIENTID integer NOT NULL references PatientDetails(PATIENTID),
  DOCTORID integer NOT NULL references DoctorDetails(DOCTORID),
  UNIQUE(PATIENTID)
);
