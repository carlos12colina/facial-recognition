# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondCalendar.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 351)
        MainWindow.setMinimumSize(QtCore.QSize(535, 351))
        MainWindow.setMaximumSize(QtCore.QSize(535, 351))
        MainWindow.setStyleSheet("background-color: rgb(255, 226, 157);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 520, 232))
        self.calendarWidget.setObjectName("calendarWidget")
        self.OK = QtWidgets.QToolButton(self.centralwidget)
        self.OK.setGeometry(QtCore.QRect(230, 260, 61, 61))
        self.OK.setStyleSheet("border-style: none;\n"
"border-width: 6px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.OK.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/images/OK.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OK.setIcon(icon)
        self.OK.setIconSize(QtCore.QSize(50, 50))
        self.OK.setObjectName("OK")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fecha final"))
