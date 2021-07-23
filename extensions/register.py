#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:32:46 2021

@author: ing-carlos
"""
import os
import sqlite3
from sqlite3 import Error
import cv2
import easygui as eg
import face_recognition

def registerPerson(name,name2,surname,surname2,ci,departament,business,phone):   
    
    dataPath ='./data/media'
    personPath = dataPath + '/' +name.upper() + '_' + name2.upper()+ '_' + surname.upper() +'_'+ surname2.upper()
    
         
    if not os.path.exists(personPath):
        con = sql_connection()
        sql_table(con,name,name2,surname,surname2,ci,departament,business,phone,personPath)
        
    else:
        eg.msgbox(msg='ya existe una persona con este nombre y apellido',title='Alerta', ok_button='Aceptar')
        

def sql_connection():

    try:

        con = sqlite3.connect('data/gcg.db')

        return con

    except Error:

        print(Error)

def sql_table(con,name,name2,surname,surname2,ci,departament,business,phone,personPath):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE if not exists employees(ci integer PRIMARY KEY,name text, second_name text, surname text, second_surname text,department text,business text,phone text)")
    cursorObj.execute("CREATE TABLE if not exists arrivals(id integer PRIMARY KEY autoincrement,date text, hour text,id_employees integer,cod_arrive text, foreign key(id_employees) references employees(ci) )")
    cursorObj.execute("CREATE TABLE if not exists departures(id integer PRIMARY KEY autoincrement,date text, hour text,id_employees integer, activityPerformed text,cod_arrive text,foreign key(id_employees) references employees(ci), foreign key(cod_arrive) references arrivals(cod_arrive) ) ")
    
    cursorObj.execute("select ci from employees where ci like "+ci)
    
    rows = cursorObj.fetchall()
    
    if rows:
        eg.msgbox(msg='Ya existe este numero de cedula',title='Alerta', ok_button='Aceptar')
   
    else:
       os.makedirs(personPath) 
       cursorObj.execute("insert into employees(ci, name, second_name, surname, second_surname,department,business,phone) values(?,?,?,?,?,?,?,?)",(ci,name.lower(),name2.lower(),surname.lower(),surname2.lower(),departament.lower(),business,phone))
       eg.msgbox(msg='Se creo la persona con exito',title='Alerta', ok_button='Aceptar')
    
    con.commit()
    con.close()
    
