# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_users.ui'
#
# Created: Thu Jul 09 13:59:09 2009
#      by: PyQt4 UI code generator 4.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    info = None
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(384, 216)
        self.lista_users = QtGui.QListWidget(Form)
        self.lista_users.setGeometry(QtCore.QRect(10, 10, 256, 192))
        self.lista_users.setObjectName("lista_users")
        self.delete_button = QtGui.QPushButton(Form)
        self.delete_button.setGeometry(QtCore.QRect(280, 90, 91, 23))
        self.delete_button.setObjectName("delete_button")

        self.retranslateUi(Form)
        
        QtCore.QMetaObject.connectSlotsByName(Form)

    def setinfo(self, item):
        info = item
        for name,password in info.items():
            self.lista_users.addItem(name+" "+password)
    
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_button.setText(QtGui.QApplication.translate("Form", "Eliminar Usuario", None, QtGui.QApplication.UnicodeUTF8))

