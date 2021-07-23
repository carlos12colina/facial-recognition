#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 08:28:58 2021

@author: ing-carlos
"""

import sqlite3
from sqlite3 import Error
import difflib

def attendanceList():
    con = sql_connection()
    data = sql_table_control(con)
    return data

def  listByfilter(startDate,finalDate,lineValue,departament,business):
    con = sql_connection()
    data = sql_table_filter(con,startDate,finalDate,lineValue,departament,business)
    return data
                    
def sql_connection():
    try:
        con = sqlite3.connect('data/gcg.db')
        return con
    
    except Error:
        print(Error)


def sql_table_control(con):
    col = 0
    rows = []
    control = []
    data = []
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "arrivals"')
    
    if cursorObj.fetchall():
        cursorObj.execute("select * from arrivals ORDER BY DATE ASC")
        arrivals = cursorObj.fetchall()
        
        for arrival in arrivals:
            
            cursorObj.execute("select * from employees where ci like ?", (arrival[3],))
            person = cursorObj.fetchall()

            cursorObj.execute("select * from departures where id_employees like ? AND cod_arrive like ?",(arrival[3],arrival[4]))
            exit = cursorObj.fetchall()

            date = arrival[1] # para obtener la fecha
            hour = arrival[2] # optener la hora 
            turno = ''
            h = arrival[2].split(":") # para saber la hora 

            if int(h[0])>17 and int(h[0])<6: # para identificar si es dia o noche 
                turno = 'N'
            else:
                turno = 'D'

            hourDeparture = 'sin marcar'
            dateDeparture = 'sin marcar'
            if exit:
                if not exit[0][2]:
                    hourDeparture = 'sin marcar'
                    dateDeparture = 'sin marcar'
                else:
                    hourDeparture = exit[0][2] #obtener la hora de salida
                    dateDeparture = exit[0][1] #obtener la fecha de salida
             

            control.extend([str(person[0][0]),person[0][1],person[0][3],date,turno,hour,dateDeparture,hourDeparture])
            rows.append(control)
            control = [] 
            col +=1

    data.append(rows)
    data.append(col)    
    con.close()

    return data


def sql_table_filter(con,startDate,finalDate,lineValue,departament,business):
    col = 0
    rows = []
    control = []
    data = []
    valuePerson=[]
    arrivals = []
    arrivals2 = []
    arrivals3 = []

    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "arrivals"')
    
    if cursorObj.fetchall():
        if startDate and finalDate and lineValue:
            
            cursorObj.execute("select * from arrivals WHERE DATE BETWEEN ? AND ? ORDER BY DATE ASC", (startDate,finalDate,))
            arrivals = cursorObj.fetchall()

            value = lineValue.split()

            if departament == 'ninguno':
                if business == 'ninguna':
                    cursorObj.execute("select * from employees where ci like ?", (value[0],))
                else:
                    cursorObj.execute("select * from employees where ci like ? AND business like ?", (value[0],business,))
            else:
                if business == 'ninguna':
                    cursorObj.execute("select * from employees where ci like ? AND department like ?", (value[0],departament,))
                else:
                    cursorObj.execute("select * from employees where ci like ? AND department like ? AND business like ?", (value[0],departament,business,))
            
            valuePerson = cursorObj.fetchall()

            if valuePerson:
                for arrival in arrivals:
                    if arrival[3] == valuePerson[0][0]:
                        arrivals2.append(arrival)

            else:
                if departament == 'ninguno':
                    if business == 'ninguna':
                        cursorObj.execute("select * from employees")
                    else:
                        cursorObj.execute("select * from employees where business like ?", (business,))
                else:
                    if business == 'ninguna':
                        cursorObj.execute("select * from employees where department like ?", (departament,))
                    else:
                        cursorObj.execute("select * from employees where department like ? AND business like ?", (departament,business,))
                
                valuePerson = cursorObj.fetchall()

                if len(value) < 2:
                    for dataPerson in valuePerson:
                        identity = dataPerson[1]+" "+ dataPerson[2]+" "+ dataPerson[3]+" "+dataPerson[4]
                        dif1 = difflib.SequenceMatcher(lambda x: x == " \t", lineValue, identity)
                        if dif1.ratio()>= 0.30:

                            for arrival in arrivals:
                                if arrival[3] == dataPerson[0]:
                                    arrivals2.append(arrival)


                else:
                    for dataPerson in valuePerson:
                        identity = dataPerson[1]+" "+ dataPerson[2]+" "+ dataPerson[3]+" "+dataPerson[4]
                        dif1 = difflib.SequenceMatcher(lambda x: x == " \t", lineValue, identity)
                        if dif1.ratio()>= 0.42:

                            for arrival in arrivals:
                                if arrival[3] == dataPerson[0]:
                                    arrivals2.append(arrival)

            arrivals = arrivals2
            

                        

        elif not lineValue and startDate and finalDate:
            if departament == 'ninguno':
                if business == 'ninguna':
                    cursorObj.execute("select * from arrivals WHERE DATE BETWEEN ? AND ? ORDER BY DATE ASC", (startDate,finalDate,))
                    arrivals = cursorObj.fetchall()
                else:
                    cursorObj.execute("select * from arrivals WHERE DATE BETWEEN ? AND ? ORDER BY DATE ASC", (startDate,finalDate,))
                    arrivals = cursorObj.fetchall()

                    for arrival in arrivals:
                        cursorObj.execute("select * from employees where ci like ?", (arrival[3],))
                        f = cursorObj.fetchall()

                        if f[0][6] == business:
                            arrivals2.append(arrival)

                    arrivals = arrivals2

            else:
                if business == 'ninguna':
                    cursorObj.execute("select * from arrivals WHERE DATE BETWEEN ? AND ? ORDER BY DATE ASC", (startDate,finalDate,))
                    arrivals = cursorObj.fetchall()

                    for arrival in arrivals:
                        cursorObj.execute("select * from employees where ci like ?", (arrival[3],))
                        f = cursorObj.fetchall()

                        if f[0][6] == departament:
                            arrivals2.append(arrival)

                    arrivals = arrivals2

                else:

                    cursorObj.execute("select * from arrivals WHERE DATE BETWEEN ? AND ? ORDER BY DATE ASC", (startDate,finalDate,))
                    arrivals = cursorObj.fetchall()

                    for arrival in arrivals:
                        cursorObj.execute("select * from employees where ci like ?", (arrival[3],))
                        f = cursorObj.fetchall()

                        if f[0][5] == departament and f[0][6] == business:
                            arrivals2.append(arrival)

                    arrivals = arrivals2



        elif lineValue and not startDate and not finalDate:
            value = lineValue.split()

            cursorObj.execute("select * from arrivals")
            arrivals = cursorObj.fetchall()

            if departament == 'ninguno':
                if business == 'ninguna':
                    cursorObj.execute("select * from employees where ci like ?", (value[0],))
                else:
                    cursorObj.execute("select * from employees where ci like ? AND business like ?", (value[0],business,))
            else:
                if business == 'ninguna':
                    cursorObj.execute("select * from employees where ci like ? AND department like ?", (value[0],departament,))
                else:
                    cursorObj.execute("select * from employees where ci like ? AND department like ? AND business like ?", (value[0],departament,business,))
            
            valuePerson = cursorObj.fetchall()
            
            if valuePerson:
                for arrival in arrivals:
                    if arrival[3] == valuePerson[0][0]:
                        arrivals2.append(arrival)
            else:
                if departament == 'ninguno':
                    if business == 'ninguna':
                        cursorObj.execute("select * from employees")
                    else:
                        cursorObj.execute("select * from employees where business like ?",(business,))
                else:
                    if business == 'ninguna':
                        cursorObj.execute("select * from employees where department like ?",(departament,))
                    else:
                        cursorObj.execute("select * from employees where department like ? AND business like ?",(departament,business,))
                
                valuePerson = cursorObj.fetchall()

                if len(value) < 2:
                    for dataPerson in valuePerson:
                        identity = dataPerson[1]+" "+ dataPerson[2]+" "+ dataPerson[3]+" "+dataPerson[4]
                        dif1 = difflib.SequenceMatcher(lambda x: x == " \t", lineValue, identity)
                        if dif1.ratio()>= 0.30:

                            for arrival in arrivals:
                                if arrival[3] == dataPerson[0]:
                                    arrivals2.append(arrival)

                else:
                    for dataPerson in valuePerson:
                        identity = dataPerson[1]+" "+ dataPerson[2]+" "+ dataPerson[3]+" "+dataPerson[4]
                        dif1 = difflib.SequenceMatcher(lambda x: x == " \t", lineValue, identity)
                        if dif1.ratio()>= 0.42:

                            for arrival in arrivals:
                                if arrival[3] == dataPerson[0]:
                                    arrivals2.append(arrival)

            arrivals = arrivals2


        elif not lineValue and not startDate and not finalDate:
            cursorObj.execute("select * from arrivals")
            arrivals = cursorObj.fetchall()

            for arrival in arrivals:
                cursorObj.execute("select * from employees where ci like ?", (arrival[3],))
                f = cursorObj.fetchall()

                if business == 'ninguna':
                    if f[0][5] == departament:
                        arrivals2.append(arrival)
                else:
                    if departament == 'ninguno':
                        if f[0][6] == business:
                            arrivals2.append(arrival)

                    else:
                        if f[0][5] == departament and f[0][6] == business:
                            arrivals2.append(arrival)

            arrivals = arrivals2

        
        for arrival in arrivals:
            cursorObj.execute("select * from employees where ci like ?", (arrival[3],))
            person = cursorObj.fetchall()

            cursorObj.execute("select * from departures where id_employees like ? AND cod_arrive like ?",(arrival[3],arrival[4]))
            exit = cursorObj.fetchall()

            date = arrival[1] # para obtener la fecha
            hour = arrival[2] # optener la hora 
            turno = ''
            h = arrival[2].split(":") # para saber la hora 

            if int(h[0])>17 and int(h[0])<6: # para identificar si es dia o noche 
                turno = 'N'
            else:
                turno = 'D'

            hourDeparture = 'sin marcar'
            dateDeparture = 'sin marcar'
            if exit:
                if not exit[0][2]:
                    hourDeparture = 'sin marcar'
                    dateDeparture = 'sin marcar'
                else:
                    hourDeparture = exit[0][2] #obtener la hora de salida
                    dateDeparture = exit[0][1] #obtener la fecha de salida
            
            control.extend([str(person[0][0]),person[0][1],person[0][3],date,turno,hour,dateDeparture,hourDeparture])
            rows.append(control)
            control = [] 
            col +=1

    data.append(rows)
    data.append(col)    
    con.close()

    return data