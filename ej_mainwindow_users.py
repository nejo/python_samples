import sys
from PyQt4 import QtGui
from mainwindow_users import *		   # Importais el formulario creado por PyQT

# Este es el esqueleto del programa principal
# Siempre es el mismo, solo cambia la el nombre de la clase del formulario, en este caso es Ui_Form
# El resto es siempre igual

# Este esqueleto es el que tendreis que llamar siempre para ejecutar la aplicacion
# Por ejemplo: python Main_boton.py


app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()	   # Creamos una ventana
ui = Ui_MainWindow()                   # <-- Aqui creamos un objeto de la clase del formulario
ui.setupUi(window)
window.show()			   # Se inicia el bucle de ejecucion principal de QT
sys.exit(app.exec_())		   # Pasa el control al motor de QT
