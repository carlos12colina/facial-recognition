# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assists.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Assists(object):
    def setupUi(self, Assists):
        Assists.setObjectName("Assists")
        Assists.setWindowModality(QtCore.Qt.NonModal)
        Assists.resize(835, 648)
        Assists.setMinimumSize(QtCore.QSize(835, 648))
        Assists.setMaximumSize(QtCore.QSize(835, 648))
        Assists.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/images/logo-gcg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Assists.setWindowIcon(icon)
        Assists.setStyleSheet("background-color: rgb(255, 226, 157);")
        Assists.setIconSize(QtCore.QSize(35, 35))
        self.centralwidget = QtWidgets.QWidget(Assists)
        self.centralwidget.setObjectName("centralwidget")
        self.tableAssists = QtWidgets.QTableWidget(self.centralwidget)
        self.tableAssists.setGeometry(QtCore.QRect(10, 240, 801, 311))
        self.tableAssists.setStyleSheet("border-style: none;\n"
"border-width: 6px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(232, 232, 232);\n"
"color: black;\n"
"border-radius: 30px;")
        self.tableAssists.setObjectName("tableAssists")
        self.tableAssists.setColumnCount(8)
        self.tableAssists.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableAssists.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAssists.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAssists.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAssists.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAssists.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAssists.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAssists.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAssists.setHorizontalHeaderItem(7, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 371, 81))
        self.label.setObjectName("label")
        self.buttonInicio = QtWidgets.QToolButton(self.centralwidget)
        self.buttonInicio.setGeometry(QtCore.QRect(580, 130, 61, 61))
        self.buttonInicio.setStyleSheet("border-style: none;\n"
"border-width: 6px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.buttonInicio.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("data/images/pngwing.com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonInicio.setIcon(icon1)
        self.buttonInicio.setIconSize(QtCore.QSize(50, 50))
        self.buttonInicio.setObjectName("buttonInicio")
        self.buttonFinal = QtWidgets.QToolButton(self.centralwidget)
        self.buttonFinal.setGeometry(QtCore.QRect(670, 130, 61, 61))
        self.buttonFinal.setStyleSheet("border-style: none;\n"
"border-width: 6px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.buttonFinal.setText("")
        self.buttonFinal.setIcon(icon1)
        self.buttonFinal.setIconSize(QtCore.QSize(50, 50))
        self.buttonFinal.setObjectName("buttonFinal")
        self.buttonSearch = QtWidgets.QToolButton(self.centralwidget)
        self.buttonSearch.setGeometry(QtCore.QRect(760, 130, 61, 61))
        self.buttonSearch.setStyleSheet("border-style: none;\n"
"border-width: 6px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.buttonSearch.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("data/images/pngwing.com(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSearch.setIcon(icon2)
        self.buttonSearch.setIconSize(QtCore.QSize(50, 50))
        self.buttonSearch.setObjectName("buttonSearch")
        self.FirtDate = QtWidgets.QLabel(self.centralwidget)
        self.FirtDate.setGeometry(QtCore.QRect(570, 190, 81, 31))
        self.FirtDate.setStyleSheet("background-color: rgb(255, 226, 157);")
        self.FirtDate.setObjectName("FirtDate")
        self.secondDate = QtWidgets.QLabel(self.centralwidget)
        self.secondDate.setGeometry(QtCore.QRect(660, 190, 81, 31))
        self.secondDate.setStyleSheet("background-color: rgb(255, 226, 157);")
        self.secondDate.setObjectName("secondDate")
        self.lineValue = QtWidgets.QLineEdit(self.centralwidget)
        self.lineValue.setGeometry(QtCore.QRect(10, 150, 331, 31))
        self.lineValue.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lineValue.setObjectName("lineValue")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 90, 391, 31))
        self.label_3.setStyleSheet("background-color: rgb(255, 226, 157);")
        self.label_3.setObjectName("label_3")
        self.FirtDate_2 = QtWidgets.QLabel(self.centralwidget)
        self.FirtDate_2.setGeometry(QtCore.QRect(20, 190, 301, 31))
        self.FirtDate_2.setStyleSheet("background-color: rgb(255, 226, 157);")
        self.FirtDate_2.setObjectName("FirtDate_2")
        self.principal = QtWidgets.QToolButton(self.centralwidget)
        self.principal.setGeometry(QtCore.QRect(750, 560, 61, 61))
        self.principal.setStyleSheet("border-style: none;\n"
"border-width: 6px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.principal.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("data/images/volver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.principal.setIcon(icon3)
        self.principal.setIconSize(QtCore.QSize(50, 50))
        self.principal.setObjectName("principal")
        self.buttontoPrint = QtWidgets.QToolButton(self.centralwidget)
        self.buttontoPrint.setGeometry(QtCore.QRect(30, 560, 61, 61))
        self.buttontoPrint.setStyleSheet("border-style: none;\n"
"border-width: 6px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.buttontoPrint.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("data/images/imprimir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttontoPrint.setIcon(icon4)
        self.buttontoPrint.setIconSize(QtCore.QSize(50, 50))
        self.buttontoPrint.setObjectName("buttontoPrint")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(360, 150, 91, 31))
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.FirtDate_3 = QtWidgets.QLabel(self.centralwidget)
        self.FirtDate_3.setGeometry(QtCore.QRect(350, 190, 111, 31))
        self.FirtDate_3.setStyleSheet("background-color: rgb(255, 226, 157);")
        self.FirtDate_3.setObjectName("FirtDate_3")
        self.comboBusiness = QtWidgets.QComboBox(self.centralwidget)
        self.comboBusiness.setGeometry(QtCore.QRect(470, 150, 91, 31))
        self.comboBusiness.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBusiness.setObjectName("comboBusiness")
        self.comboBusiness.addItem("")
        self.comboBusiness.addItem("")
        self.comboBusiness.addItem("")
        self.comboBusiness.addItem("")
        self.comboBusiness.addItem("")
        self.comboBusiness.addItem("")
        self.FirtDate_4 = QtWidgets.QLabel(self.centralwidget)
        self.FirtDate_4.setGeometry(QtCore.QRect(460, 190, 111, 31))
        self.FirtDate_4.setStyleSheet("background-color: rgb(255, 226, 157);")
        self.FirtDate_4.setObjectName("FirtDate_4")
        Assists.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Assists)
        self.statusbar.setObjectName("statusbar")
        Assists.setStatusBar(self.statusbar)

        self.retranslateUi(Assists)
        QtCore.QMetaObject.connectSlotsByName(Assists)

    def retranslateUi(self, Assists):
        _translate = QtCore.QCoreApplication.translate
        Assists.setWindowTitle(_translate("Assists", "Asistencias"))
        item = self.tableAssists.horizontalHeaderItem(0)
        item.setText(_translate("Assists", "Cedula"))
        item = self.tableAssists.horizontalHeaderItem(1)
        item.setText(_translate("Assists", "Nombre"))
        item = self.tableAssists.horizontalHeaderItem(2)
        item.setText(_translate("Assists", "Apellido"))
        item = self.tableAssists.horizontalHeaderItem(3)
        item.setText(_translate("Assists", "Fecha"))
        item = self.tableAssists.horizontalHeaderItem(4)
        item.setText(_translate("Assists", "Turno"))
        item = self.tableAssists.horizontalHeaderItem(5)
        item.setText(_translate("Assists", "Hora Inicio"))
        item = self.tableAssists.horizontalHeaderItem(6)
        item.setText(_translate("Assists", "Fecha salida"))
        item = self.tableAssists.horizontalHeaderItem(7)
        item.setText(_translate("Assists", "Hora salida"))
        self.label.setText(_translate("Assists", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-style:italic;\">Control de asistencias</span></p></body></html>"))
        self.FirtDate.setText(_translate("Assists", "<html><head/><body><p align=\"center\">Inicio</p></body></html>"))
        self.secondDate.setText(_translate("Assists", "<html><head/><body><p align=\"center\">Final</p></body></html>"))
        self.label_3.setText(_translate("Assists", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic;\">Filtrar por Nombre, Cedula, Departamento o Fecha </span></p></body></html>"))
        self.FirtDate_2.setText(_translate("Assists", "<html><head/><body><p align=\"center\">Ingrese el nombre o cedula de la persona</p></body></html>"))
        self.comboBox.setItemText(0, _translate("Assists", "ninguno"))
        self.comboBox.setItemText(1, _translate("Assists", "sistemas"))
        self.comboBox.setItemText(2, _translate("Assists", "administración"))
        self.comboBox.setItemText(3, _translate("Assists", "gerencia"))
        self.comboBox.setItemText(4, _translate("Assists", "compras"))
        self.comboBox.setItemText(5, _translate("Assists", "recursos humanos"))
        self.comboBox.setItemText(6, _translate("Assists", "mantenimiento y limpieza"))
        self.FirtDate_3.setText(_translate("Assists", "<html><head/><body><p align=\"center\">Departamento</p></body></html>"))
        self.comboBusiness.setItemText(0, _translate("Assists", "ninguna"))
        self.comboBusiness.setItemText(1, _translate("Assists", "VENSUCA"))
        self.comboBusiness.setItemText(2, _translate("Assists", "GCG PROVEEDORES"))
        self.comboBusiness.setItemText(3, _translate("Assists", "FULL TOOLS"))
        self.comboBusiness.setItemText(4, _translate("Assists", "MTN"))
        self.comboBusiness.setItemText(5, _translate("Assists", "SUMIVENTA"))
        self.FirtDate_4.setText(_translate("Assists", "<html><head/><body><p align=\"center\">Empresa</p></body></html>"))
