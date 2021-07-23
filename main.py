# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(821, 648)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(821, 648))
        MainWindow.setMaximumSize(QtCore.QSize(821, 648))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/images/logo-gcg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(-5.0)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 226, 157);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.GroupedDragging)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 110, 441, 421))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("data/images/logo-gcg.png"))
        self.label.setObjectName("label")
        self.reconocer = QtWidgets.QToolButton(self.centralwidget)
        self.reconocer.setGeometry(QtCore.QRect(20, 30, 161, 161))
        self.reconocer.setStyleSheet("border-style: none;\n"
"border-width: 6px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 80px;")
        self.reconocer.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("data/images/reconocer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reconocer.setIcon(icon1)
        self.reconocer.setIconSize(QtCore.QSize(150, 150))
        self.reconocer.setObjectName("reconocer")
        self.register_2 = QtWidgets.QToolButton(self.centralwidget)
        self.register_2.setGeometry(QtCore.QRect(20, 240, 161, 161))
        self.register_2.setStyleSheet("border-style: none;\n"
"border-width: 6px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 80px;")
        self.register_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("data/images/agregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.register_2.setIcon(icon2)
        self.register_2.setIconSize(QtCore.QSize(150, 150))
        self.register_2.setObjectName("register_2")
        self.AssistsList = QtWidgets.QToolButton(self.centralwidget)
        self.AssistsList.setGeometry(QtCore.QRect(20, 450, 161, 161))
        self.AssistsList.setStyleSheet("border-style: none;\n"
"border-width: 6px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 80px;")
        self.AssistsList.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("data/images/lista.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AssistsList.setIcon(icon3)
        self.AssistsList.setIconSize(QtCore.QSize(150, 150))
        self.AssistsList.setObjectName("AssistsList")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reconocimiento facial"))
