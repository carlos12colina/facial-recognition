#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:32:46 2021

@author: ing-carlos
"""

import cv2
import face_recognition
import easygui as eg
import sqlite3
from sqlite3 import Error
from datetime import datetime

def recognizer():
    
    OriginPath = "data/media/"
    con = sql_connection()
    rows = sql_table(con)
    
    name = ''
    surname = ''
    second_name = ''
    second_surname = ''
    directories = []
    identification = []
    images = []
    encodings = []
    
    for row in rows:
        Path = OriginPath
        cont = 0
        
        for data in row:
            if cont == 1:
                name = data.upper()
            if cont == 2:
                second_name = data.upper()
            if cont == 3:
                surname = data.upper()
            if cont == 4:
                second_surname = data.upper()
            if cont == 5:
                Path = Path+name+"_"+second_name+"_"+surname+"_"+second_surname+"/foto.jpg"
                directories.append(Path)
                identity = name +" "+second_name+" "+surname+" "+second_surname
                identification.append(identity)

            cont += 1
            
    
    for directory in directories:
        imagen_personal = face_recognition.load_image_file(directory)
        images.append(imagen_personal)
        
    for image in images:
        encoding = face_recognition.face_encodings(image)[0]
        encodings.append(encoding)
         
    
    
    encodings_conocidos = encodings
    
    nombres_conocidos = identification
         
    #Iniciar la webcam:
    webcam = cv2.VideoCapture(0)


    if not webcam.isOpened():
        eg.msgbox(msg='Conecte una camara y reinicie el sistema',title='Alerta', ok_button='Aceptar')
    else:
        # NOTA: Si no funciona puedes cambiar el índice '0' por otro, o cambiarlo por la dirección de tu webcam.
        #Cargar una fuente de texto:
        font = cv2.FONT_HERSHEY_COMPLEX
                
                 
        # Identificar rostros es un proceso costoso. Para poder hacerlo en tiempo real sin que haya retardo
        # vamos a reducir el tamaño de la imagen de la webcam. Esta variable 'reduccion' indica cuanto se va a reducir:
        reduccion = 5 #Con un 5, la imagen se reducirá a 1/5 del tamaño original
                
                
        #Recordamos al usuario cuál es la tecla para salir:
        print("\nRecordatorio: pulsa 'ESC' para cerrar.\n")
                
                
        while 1:
            #Definimos algunos arrays y variables:
            loc_rostros = [] #Localizacion de los rostros en la imagen
            encodings_rostros = [] #Encodings de los rostros
            nombres_rostros = [] #Nombre de la persona de cada rostro
            nombre = "" #Variable para almacenar el nombre
                
            #Capturamos una imagen con la webcam:
            valido, img = webcam.read()


                
            #Si la imagen es válida (es decir, si se ha capturado correctamente), continuamos:
            if valido:
              
                #La imagen está en el espacio de color BGR, habitual de OpenCV. Hay que convertirla a RGB:
                img_rgb = img[:, :, ::-1]
             
                #Reducimos el tamaño de la imagen para que sea más rápida de procesar:
                img_rgb = cv2.resize(img_rgb, (0, 0), fx=1.0/reduccion, fy=1.0/reduccion)
              
                #Localizamos cada rostro de la imagen y extraemos sus encodings:
                loc_rostros = face_recognition.face_locations(img_rgb)
                encodings_rostros = face_recognition.face_encodings(img_rgb, loc_rostros)
                
                #Recorremos el array de encodings que hemos encontrado:
                for encoding in encodings_rostros:
              
                    #Buscamos si hay alguna coincidencia con algún encoding conocido:
                    coincidencias = face_recognition.compare_faces(encodings_conocidos, encoding)
                
                    #El array 'coincidencias' es ahora un array de booleanos. Si contiene algun 'True', es que ha habido alguna coincidencia:
                    if True in coincidencias:
                        nombre = nombres_conocidos[coincidencias.index(True)]
             
                    #Si no hay ningún 'True' en el array 'coincidencias', no se ha podido identificar el rostro:
                    else:
                        nombre = "Sin registro"
                 
                    #Añadir el nombre de la persona identificada en el array de nombres:
                    nombres_rostros.append(nombre)
                 
                #Dibujamos un recuadro rojo alrededor de los rostros desconocidos, y uno verde alrededor de los conocidos:
                for (top, right, bottom, left), nombre in zip(loc_rostros, nombres_rostros):
                             
                    #Deshacemos la reducción de tamaño para tener las coordenadas de la imagen original:
                    top = top*reduccion
                    right = right*reduccion
                    bottom = bottom*reduccion
                    left = left*reduccion
                 
                    #Cambiar de color según si se ha identificado el rostro:
                    if nombre != "Sin registro":
                        color = (0,255,0)
                    else:
                        color = (0,0,255)
                                #Dibujar un rectángulo alrededor de cada rostro identificado, y escribir el nombre:
                    cv2.rectangle(img, (left + 10, top), (right + 10, bottom), color, 2)
                    cv2.rectangle(img, (left - 80, bottom - 20), (right + 150, bottom), color, -1)
                    cv2.putText(img, nombre, (left - 50, bottom - 6), font, 0.6, (0,0,0), 1)
                              #Mostrar el resultado en una ventana:
                cv2.imshow('Presione enter si ve su nombre el recuadro', img)
                 
                #Salir con 'ESC'
                k =  cv2.waitKey(5) & 0xFF
                if k == 27:
                    cv2.destroyAllWindows()
                    break
                        
                if k == 13 and nombre != "Sin registro" and nombre != "":
                    con = sql_connection()
                    data = nombre.lower()
                    person = data.split()
                    sql_table_date(con,person)

            else:
                cv2.destroyAllWindows()
                eg.msgbox(msg='Conecte una camara y reinicie el sistema',title='Alerta', ok_button='Aceptar')
                break
                 
        webcam.release()

    
    
    
    

def sql_connection():

    try:
        con = sqlite3.connect('data/gcg.db')

        return con

    except Error:

        print(Error)
        

def sql_table(con):
    rows = []
    cursorObj = con.cursor()
    
    cursorObj.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "employees"')

    if cursorObj.fetchall():
        cursorObj.execute("select * from employees")
        rows = cursorObj.fetchall()
        con.commit()          
    
   
    con.close()
    return rows

def sql_table_date(con,person):
    cursorObj = con.cursor()
    openDay = 0
    today = 0
    
    cursorObj.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "employees"')

    if cursorObj.fetchall():
        cursorObj.execute("SELECT * FROM employees WHERE name = ? AND second_name = ? AND surname = ? AND second_surname = ?", (person[0],person[1],person[2],person[3]))
        rows = cursorObj.fetchall()
        now = datetime.now()
        
        date_time = now.strftime("%Y-%m-%d")
        hour = now.strftime("%H:%M:%S")

        cod_arrive = date_time+'-'+hour+'-'+str(rows[0][0])

        cursorObj.execute("SELECT * FROM departures  WHERE id_employees= ? ORDER BY id DESC", (rows[0][0],))
        dataDeparture = cursorObj.fetchall()

        if dataDeparture:        
            if not dataDeparture[0][1]:
                openDay = 1

        if openDay:
            cursorObj.execute("UPDATE departures SET date = ?,hour = ? WHERE cod_arrive = ?", (date_time,hour,dataDeparture[0][5],))
            eg.msgbox(msg='Ah firmado su salida como '+rows[0][1]+' '+rows[0][3],title='Alerta', ok_button='Aceptar')
        else:
            cursorObj.execute("INSERT INTO arrivals(date,hour,id_employees,cod_arrive) VALUES(?,?,?,?)",(date_time,hour,rows[0][0],cod_arrive,))
            cursorObj.execute("INSERT INTO departures(id_employees,cod_arrive) VALUES(?,?)",(rows[0][0],cod_arrive,))
            eg.msgbox(msg='Ah firmado su entrada como '+rows[0][1]+' '+rows[0][3],title='Alerta', ok_button='Aceptar')
                

        
        con.commit()

        #date = date_time.split()
        #dat = date[1].split(":")
        #print(dat)       
    
    con.close()