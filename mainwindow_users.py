# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_users.ui'
#
# Created: Thu Jul 09 13:52:31 2009
#      by: PyQt4 UI code generator 4.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import list_users

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(282, 176)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.name_label = QtGui.QLabel(self.centralwidget)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.name_text = QtGui.QLineEdit(self.centralwidget)
        self.name_text.setObjectName("name_text")
        self.gridLayout.addWidget(self.name_text, 0, 1, 1, 1)
        self.password_label = QtGui.QLabel(self.centralwidget)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 1, 0, 1, 1)
        self.password_text = QtGui.QLineEdit(self.centralwidget)
        self.password_text.setEchoMode(QtGui.QLineEdit.Password)
        self.password_text.setObjectName("password_text")
        self.gridLayout.addWidget(self.password_text, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 3)
        self.add_button = QtGui.QPushButton(self.centralwidget)
        self.add_button.setObjectName("add_button")
        self.gridLayout_2.addWidget(self.add_button, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 32, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 2, 1, 1)
        self.view_button = QtGui.QPushButton(self.centralwidget)
        self.view_button.setObjectName("view_button")
        self.gridLayout_2.addWidget(self.view_button, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(196, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 1, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(196, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 282, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.actionGuardar_usuarios = QtGui.QAction(MainWindow)
        self.actionGuardar_usuarios.setObjectName("actionGuardar_usuarios")
        self.actionCargar_usuarios = QtGui.QAction(MainWindow)
        self.actionCargar_usuarios.setObjectName("actionCargar_usuarios")
        self.menuArchivo.addAction(self.actionGuardar_usuarios)
        self.menuArchivo.addAction(self.actionCargar_usuarios)
        self.menubar.addAction(self.menuArchivo.menuAction())
        
        self.users = {}

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.add_button,QtCore.SIGNAL("clicked()"),self.add)
        QtCore.QObject.connect(self.view_button,QtCore.SIGNAL("clicked()"),self.view)
        QtCore.QObject.connect(self.actionGuardar_usuarios,QtCore.SIGNAL("clicked()"),self.save)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Gestión de Usuarios", None, QtGui.QApplication.UnicodeUTF8))
        self.name_label.setText(QtGui.QApplication.translate("MainWindow", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.password_label.setText(QtGui.QApplication.translate("MainWindow", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.add_button.setText(QtGui.QApplication.translate("MainWindow", "Agregar Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.view_button.setText(QtGui.QApplication.translate("MainWindow", "Visualizar Usuarios", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivo.setTitle(QtGui.QApplication.translate("MainWindow", "Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar_usuarios.setText(QtGui.QApplication.translate("MainWindow", "Guardar usuarios", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCargar_usuarios.setText(QtGui.QApplication.translate("MainWindow", "Cargar usuarios", None, QtGui.QApplication.UnicodeUTF8))

    def add(self):
        self.users[self.name_text.text()] = self.password_text.text()
        self.name_text.setText("")
        self.password_text.setText("")
    
    def view (self):
        win_list = QtGui.QDialog()	   # Creamos una ventana
        mw = list_users.Ui_Form()
        mw.setupUi(win_list)
        mw.setinfo(self.users)        # pasamos la información al otro formulario
        
        win_list.exec_()			        # Se inicia el bucle de ejecucion principal de QT
    
    def save(self):
        print "save" # pickle