# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Wed Nov  6 15:03:05 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 481)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.fire_button = QtWidgets.QPushButton(self.centralWidget)
        self.fire_button.setGeometry(QtCore.QRect(40, 310, 181, 61))
        self.fire_button.setObjectName("fire_button")
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 40, 241, 41))
        self.comboBox.setObjectName("comboBox")
        self.target_x = QtWidgets.QLCDNumber(self.centralWidget)
        self.target_x.setGeometry(QtCore.QRect(80, 110, 64, 23))
        self.target_x.setObjectName("target_x")
        self.target_y = QtWidgets.QLCDNumber(self.centralWidget)
        self.target_y.setGeometry(QtCore.QRect(80, 140, 64, 23))
        self.target_y.setObjectName("target_y")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(60, 110, 16, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 16, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 111, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(60, 190, 111, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(60, 210, 16, 17))
        self.label_5.setObjectName("label_5")
        self.current_x = QtWidgets.QLCDNumber(self.centralWidget)
        self.current_x.setGeometry(QtCore.QRect(80, 210, 64, 23))
        self.current_x.setObjectName("current_x")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(60, 240, 16, 17))
        self.label_6.setObjectName("label_6")
        self.current_y = QtWidgets.QLCDNumber(self.centralWidget)
        self.current_y.setGeometry(QtCore.QRect(80, 240, 64, 23))
        self.current_y.setObjectName("current_y")
        self.new_position_name = QtWidgets.QLineEdit(self.centralWidget)
        self.new_position_name.setGeometry(QtCore.QRect(330, 40, 201, 41))
        self.new_position_name.setObjectName("new_position_name")
        self.new_position_butotn = QtWidgets.QPushButton(self.centralWidget)
        self.new_position_butotn.setGeometry(QtCore.QRect(340, 90, 181, 61))
        self.new_position_butotn.setObjectName("new_position_butotn")
        self.update_position_button = QtWidgets.QPushButton(self.centralWidget)
        self.update_position_button.setGeometry(QtCore.QRect(340, 310, 181, 61))
        self.update_position_button.setObjectName("update_position_button")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 561, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.fire_button.setText(QtWidgets.QApplication.translate("MainWindow", "FIRE", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "X", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Y", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Target Position", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Current Position", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "X", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Y", None, -1))
        self.new_position_butotn.setText(QtWidgets.QApplication.translate("MainWindow", "Create New", None, -1))
        self.update_position_button.setText(QtWidgets.QApplication.translate("MainWindow", "Update Position", None, -1))

