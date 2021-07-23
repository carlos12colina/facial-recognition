#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys,re,cv2
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from screeninfo import get_monitors
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.QtGui import QIcon, QFont, QTextDocument
from PyQt5.QtCore import Qt, QFileInfo, QTextCodec, QByteArray, QTranslator, QLocale, QLibraryInfo
from PyQt5.QtWidgets import (QApplication, QTreeWidget, QTreeWidgetItem, QDialog, QPushButton, QFileDialog,
                             QMessageBox, QToolBar)
import easygui as eg
from extensions import recognizer
from extensions import register
from extensions import attendanceList

# IMPORTAMOS LA INTERFACE .PY
import assists
import firstCalendar 
import secondCalendar
import registerView
import main


#qtCreatorFile = "data/views/main.ui" # Nombre del archivo aquí.

#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Main(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Main, self).__init__()
        #loadUi('data/views/main.ui', self)
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)
        monitors = get_monitors()
        self.move((monitors[0].width - self.width())/ 2, (monitors[0].height - self.height()) /2);
        self.ui.reconocer.clicked.connect(self.accion)
        self.ui.register_2.clicked.connect(self.accion2)
        self.ui.AssistsList.clicked.connect(self.accion3)
        
    def accion(self):
        recognizer.recognizer()
        
    def accion2(self):
        self.hide()
        self.ventana = RegisterWindow(self.ui)
        self.ventana.show()
    
    def accion3(self):
        self.hide()
        self.ventana = AssistsWindow(self.ui)
        self.ventana.show()

class RegisterWindow(QtWidgets.QMainWindow):
        
     def __init__(self,parent=None):
         super(RegisterWindow, self).__init__()
         self.ui = registerView.Ui_Register()
         self.ui.setupUi(self)
         monitors = get_monitors()
         self.move((monitors[0].width - self.width())/ 2, (monitors[0].height - self.height()) /2);
         self.ui.principal.clicked.connect(self.accion)
         self.ui.register_2.clicked.connect(self.accion2)
         self.ui.textName.textChanged.connect(self.validar_name)
         self.ui.textName_2.textChanged.connect(self.validar_name2)
         self.ui.textSurname.textChanged.connect(self.validar_surname)
         self.ui.textSurname_2.textChanged.connect(self.validar_surname2)
         self.ui.textCi.textChanged.connect(self.validar_ci)
         self.ui.textPhone.textChanged.connect(self.validar_phone)

         self.camera = 1

          # CREAMOS UNA VARIABLE DONDE SE VA A GUARDAR LA IMAGEN
         self.imagen = None
         
         # INICIAMOS LA CAMARA WEB
         # SE UTILIZA LA 0 YA QUE ES LA QUE CORRESPONDE A LA WEBCAM
         # SI QUIEREN USAR OTRA SOLO INVESTIGUEN QUE INDICE TIENE
         # Y CAMBIENLA EN cv2.VideoCapture(?)
         self.ui.captura = cv2.VideoCapture(0)

         # DEFINIMOS EL TAMAÑO DONDE SE VA A MOSTRAR LA IMAGEN
         # ESOS VALORES YO LOS TOME DE EL TAMAÑO DE EL QLABEL EN QUE SE MUESTRA
         self.ui.captura.set(cv2.CAP_PROP_FRAME_HEIGHT, 451)
         self.ui.captura.set(cv2.CAP_PROP_FRAME_WIDTH, 711)

         # SE CREA UN TIMER PARA QUE VAYA ACTUALIZANDO LA IMAGEN EN EL QLABEL
         self.timer = QTimer()

         # SE MANDA A LLAMAR EL METODO PARA MANDAR LA IMAGEN
         self.timer.timeout.connect(self.actualizar)
         self.timer.start(1)
         

         self.name = ''
         self.name2 = ''
         self.surname = ''
         self.surname2 = ''
         self.ci = ''
         self.phone = ''

         value = self.ui.comboBox.currentText()

         
     # METODO PARA ACTUALIZAR LA IMAGEN
     def actualizar(self):
        try:
            ret, self.imagen = self.ui.captura.read()
            self.imagen = cv2.flip(self.imagen, 1)

            # SE MANDA A LLAMAR EL METODO MOSTRAR IMAGEN PASANDO 2 PARAMETROS
            self.mostrar_imagen(self.imagen, 1)

            self.camera = 1
        except:
            if self.camera == 1:
                window.show()
                self.ui.captura.release()
                self.close()
                self.camera = 0
                eg.msgbox(msg='Conecte una camara y reinicie el sistema',title='Alerta', ok_button='Aceptar')
            

     # METODO PARA MOSTRAR LA IMAGEN EN EL QLABEL
     def mostrar_imagen(self, imagen, ventana=1):
        formato = QImage.Format_Indexed8

        if len(imagen.shape) == 3:
            if imagen.shape == 4:
                formato = QImage.Format_RGBA8888
            else:
                formato = QImage.Format_RGB888

        salida = QImage(imagen, imagen.shape[1], imagen.shape[0], imagen.strides[0], formato)
        salida = salida.rgbSwapped()

        if ventana == 1:
            self.ui.Mostrar.setPixmap(QPixmap.fromImage(salida))
            self.ui.Mostrar.setScaledContents(True)
     
     def accion(self):
         window.show()
         self.timer.stop()
         self.ui.captura.release()
         self.close()
         
     def validar_name(self):
         name = self.ui.textName.toPlainText()
         validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', name, re.I)
         
         if name=="":
             self.name = ''
             self.ui.textName.setStyleSheet("background: 1px solid #e5ff63;")
             return False
         elif not validar:
            self.name = ''
            self.ui.textName.setStyleSheet("background: 1px solid #ff5d52;")
            return False
         else:
             self.name = name
             self.ui.textName.setStyleSheet("background: 1px solid #8aff8e;")
             return True

     def validar_name2(self):
         name2 = self.ui.textName_2.toPlainText()
         validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', name2, re.I)
         
         if name2=="":
             self.name2 = ''
             self.ui.textName_2.setStyleSheet("background: 1px solid #e5ff63;")
             return False
         elif not validar:
            self.name2 = ''
            self.ui.textName_2.setStyleSheet("background: 1px solid #ff5d52;")
            return False
         else:
             self.name2 = name2
             self.ui.textName_2.setStyleSheet("background: 1px solid #8aff8e;")
             return True
        
     def validar_surname(self):
         surname = self.ui.textSurname.toPlainText()
         validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', surname, re.I)
         
         if surname=="":
             self.surname = ''
             self.ui.textSurname.setStyleSheet("background: 1px solid #e5ff63;")
             return False
         elif not validar:
            self.surname = ''
            self.ui.textSurname.setStyleSheet("background: 1px solid #ff5d52;")
            return False
         else:
             self.surname = surname
             self.ui.textSurname.setStyleSheet("background: 1px solid #8aff8e;")
             return True

     def validar_surname2(self):
         surname2 = self.ui.textSurname_2.toPlainText()
         validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', surname2, re.I)
         
         if surname2=="":
             self.surname2 = ''
             self.ui.textSurname_2.setStyleSheet("background: 1px solid #e5ff63;")
             return False
         elif not validar:
             self.surname2 = ''
             self.ui.textSurname_2.setStyleSheet("background: 1px solid #ff5d52;")
             return False
         else:
             self.surname2 = surname2
             self.ui.textSurname_2.setStyleSheet("background: 1px solid #8aff8e;")
             return True
         
     def validar_ci(self):
         ci = self.ui.textCi.toPlainText()
         validar = re.match('^[0-9\sáéíóúàèìòùäëïöüñ]+$', ci, re.I)
         
         if ci=="":
             self.ci = ''
             self.ui.textCi.setStyleSheet("background: 1px solid #e5ff63;")
             return False
         elif not validar:
             self.ci = ''
             self.ui.textCi.setStyleSheet("background: 1px solid #ff5d52;")
             return False
         else:
             self.ci = ci
             self.ui.textCi.setStyleSheet("background: 1px solid #8aff8e;")
             return True
         
     def validar_phone(self):
         phone = self.ui.textPhone.toPlainText()
         validar = re.match('^[0-9\sáéíóúàèìòùäëïöüñ]+$',phone, re.I)
         
         if phone=="":
             self.phone = ''
             self.ui.textPhone.setStyleSheet("background: 1px solid #e5ff63;")
             return False
         elif not validar:
             self.phone = ''
             self.ui.textPhone.setStyleSheet("background: 1px solid #ff5d52;")
             return False
         else:
             self.phone = phone
             self.ui.textPhone.setStyleSheet("background: 1px solid #8aff8e;")
             return True
         
     def accion2(self):
         if self.camera:
             if self.name and self.name2 and self.surname and self.surname2 and self.ci and self.phone:
                 register.registerPerson(self.ui.textName.toPlainText(),self.ui.textName_2.toPlainText(),self.ui.textSurname.toPlainText(),self.ui.textSurname_2.toPlainText(),self.ui.textCi.toPlainText(),self.ui.comboBox.currentText(),self.ui.comboBusiness.currentText(),self.ui.textPhone.toPlainText())
                 cv2.imwrite('./data/media'+'/' +self.name.upper()+'_'+self.name2.upper()+'_'+self.surname.upper()+'_'+self.surname2.upper()+"/foto.jpg", self.imagen)
                 self.ui.textName.setText('')
                 self.ui.textName_2.setText('')
                 self.ui.textSurname.setText('')
                 self.ui.textSurname_2.setText('')
                 self.ui.textCi.setText('')
                 self.ui.textPhone.setText('')
             else:
                 eg.msgbox(msg='Verifique que los campos estén correctamente',title='Alerta', ok_button='Aceptar')
         else:
            eg.msgbox(msg='Conecte una camara y reinicie el sistema',title='Alerta', ok_button='Aceptar')

            
class   AssistsWindow(QtWidgets.QMainWindow):
        
     def __init__(self,parent=None):
        
         super(AssistsWindow, self).__init__()
         self.ui = assists.Ui_Assists()
         self.ui.setupUi(self)

         monitors = get_monitors()
         self.move((monitors[0].width - self.width())/ 2, (monitors[0].height - self.height()) /2);
         self.ui.principal.clicked.connect(self.shutDown)
         self.ui.buttonInicio.clicked.connect(self.startCalendar)
         self.ui.buttonFinal.clicked.connect(self.finalCalendar)
         self.ui.buttonSearch.clicked.connect(self.search)
         self.ui.buttontoPrint.clicked.connect(self.toPrint)

         global startDate
         startDate = ''

         global finalDate
         finalDate = ''

         self.data = ''

         self.departamento =''
         
         self.empresa =''


                 
     def shutDown(self):
         window.show()
         self.close()
         
     def startCalendar(self):
        
        self.ventana = startCalendar(self.ui)
        self.ventana.show()
    
     def finalCalendar(self):
        self.ventana = finalCalendar(self.ui)
        self.ventana.show()

     def search(self):

        self.ui.tableAssists.clearContents()

        if self.ui.comboBox.currentText() == 'ninguno':
            self.departamento = ''
        else:
            self.departamento = self.ui.comboBox.currentText()
            
        if self.ui.comboBusiness.currentText() == 'ninguna':
            self.empresa = ''
        else:
            self.empresa = self.ui.comboBusiness.currentText()

        self.data = attendanceList.listByfilter(startDate,finalDate,self.ui.lineValue.text(),self.ui.comboBox.currentText(),self.ui.comboBusiness.currentText())

        rows = self.data[0]

        self.ui.tableAssists.setColumnCount(8)
            
        self.ui.tableAssists.setRowCount(self.data[1])
             
        row=0

        for tup in rows:

            col=0

            for item in tup:

                cellinfo=QTableWidgetItem(item)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled) # para que no sea editable
                self.ui.tableAssists.setItem(row, col, cellinfo)
                col+=1

            row += 1

     def toPrint(self):
        self.documento = QTextDocument()

        self.documento.clear()
        datos = ""
        if self.data:
            for dato in self.data[0]:
                datos += "<tr><td>"+dato[0]+"</td><td>"+dato[1]+"</td><td>"+dato[2]+"</td><td>"+dato[3]+"</td><td>"+dato[4]+"</td><td>"+dato[5]+"</td><td>"+dato[6]+"</td><td>"+dato[7]+"</td></tr>"

            reporteHtml = """
                <!DOCTYPE html>
                <html>
                <head>
                <meta charset="UTF-8">
                <style>
                h3 {
                    font-family: Helvetica-Bold;
                    text-align: center;
                   }

                table {
                       font-family: arial, sans-serif;
                       border-collapse: collapse;
                       width: 100%;
                       border-radius: 30px;
                      }

                td {
                    text-align: left;
                    padding-top: 4px;
                    padding-right: 6px;
                    padding-bottom: 2px;
                    padding-left: 6px;
                   }

                th {
                    text-align: left;
                    padding: 4px;
                    background-color: black;
                    color: white;
                   }

                tr {
                    text-align: left;
                    padding: 4px;
                    background-color: black;
                    color: black;
                    background:white
                   }


                tr:nth-child(even) {
                                    background-color: #dddddd;
                                   }
                </style>
                </head>
                <body>

                <h3>Listado de asistencia [Empresa]<br/></h3>

                <table align="left" width="100%" cellspacing="0">
                  <tr>
                    <th>C.I</th>
                    <th>Nombre</th>
                    <th>Apellido</th>
                    <th>Fecha inicio</th>
                    <th>Turno</th>
                    <th>Hora inicio</th>
                    <th>Fecha salida</th>
                    <th>Hora salida</th>
                  </tr>
                  [DATOS]
                </table>

                </body>
                </html>
                """.replace("[DATOS]", datos).replace("[Empresa]",self.empresa)
                

            datos = QByteArray()
            datos.append(str(reporteHtml))
            codec = QTextCodec.codecForHtml(datos)
            unistr = codec.toUnicode(datos)

            if Qt.mightBeRichText(unistr):
                self.documento.setHtml(unistr)
            else:
                self.documento.setPlainText(unistr)

            if not self.documento.isEmpty():
                nombreArchivo, _ = QFileDialog.getSaveFileName(self, "Exportar a PDF", "Asistencia",
                                                               "Archivos PDF (*.pdf)",
                                                               options=QFileDialog.Options())

            if nombreArchivo:
                impresion = QPrinter(QPrinter.HighResolution)
                impresion.setOutputFormat(QPrinter.PdfFormat)
                impresion.setOutputFileName(nombreArchivo)
                self.documento.print_(impresion)
                eg.msgbox(msg='Se ha guardado con exito',title='Alerta', ok_button='Aceptar')
                   


         
class   startCalendar(QtWidgets.QMainWindow):
        
     def __init__(self,parent=None):
         super(startCalendar, self).__init__()
         self.ui = firstCalendar.Ui_MainWindow()
         self.ui.setupUi(self)
         monitors = get_monitors()
         self.move((monitors[0].width - self.width())/ 2, (monitors[0].height - self.height()) /2);
         self.ui.OK.clicked.connect(self.selectDate)
         self.parent = parent
         

     def selectDate(self):
        date = self.ui.calendarWidget.selectedDate()
        dateString = str(date.toPyDate())

        global startDate
        startDate = dateString
        self.parent.FirtDate.setText(startDate)
        self.close()

class   finalCalendar(QtWidgets.QMainWindow):
        
     def __init__(self,parent=None):
         super(finalCalendar, self).__init__()
         self.ui = secondCalendar.Ui_MainWindow()
         self.ui.setupUi(self)
         monitors = get_monitors()
         self.move((monitors[0].width - self.width())/ 2, (monitors[0].height - self.height()) /2);
         self.ui.OK.clicked.connect(self.selectDate)
         self.parent = parent
         
     def selectDate(self):
        date = self.ui.calendarWidget.selectedDate()
        dateString = str(date.toPyDate())

        global finalDate
        finalDate = dateString
        self.parent.secondDate.setText(finalDate)
        self.close()

app = QtWidgets.QApplication(sys.argv)
window = Main()
window.show()
app.exec_()
