# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
import geopandas as gpd
import pandas as pd
from message import error_msg

class UI_FileDialog(object):
    COORDINATE_LIST = ['unknown', 'WGS84', 'BJ54', 'XIAN80', 'CGCS2000']

    def setupUi(self, Dialog):
        self.path = ''
        self.coord = ''
        self.ext = ''
        self.gdf = None
        Dialog.setObjectName("Dialog")
        Dialog.resize(423, 301)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.clicked.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 341, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QLineEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.coordinateSelect = QtWidgets.QComboBox(Dialog)
        self.coordinateSelect.setGeometry(QtCore.QRect(30, 110, 231, 28))
        self.coordinateSelect.setObjectName("coordinateSelect")
        self.coordinate_init()

        self.retranslateUi(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "open file"))


    def coordinate_init(self):
        self.coordinateSelect.addItems(self.COORDINATE_LIST)