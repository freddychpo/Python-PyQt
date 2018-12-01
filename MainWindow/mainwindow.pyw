# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 14:37:28 2018

@author: FREDDY
"""


import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Metodo constructor de la clase
    def __init__(self):
        #iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #cargar la configuracion del archivo .ui en el objeto 
        uic.loadUi("MainWindow.ui", self)
        
#Instancia para iniciar una aplicacion
app = QApplication(sys.argv)

#Crear un objeto de clase 
_ventana = Ventana()

#Mostrar las ventana
_ventana.show()

#Ejecutar la aplicacion 
app.exec()
