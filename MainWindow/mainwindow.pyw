# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 14:37:28 2018

@author: FREDDY
"""

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic 
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import ctypes #GetSystemMetrics

#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Metodo constructor de la clase
    def __init__(self):
        #iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #cargar la configuracion del archivo .ui en el objeto 
        uic.loadUi("MainWindow.ui", self)
        self.setWindowTitle("Calc de propinas")
        #Mostrar la ventana maximizada
        self.showMaximized()
        #Fijar el tamano de la ventana
        #Fijar el tamano minimo
        self.setMinimumSize(425, 250)
        #Fijar el tamano maximo
        self.setMaximumSize(425,250)
        
        #Mover la ventana y centrarla en el escritorio
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)
        left = (resolucion_ancho / 2) - (self.frameSize().width()/2)
        top = (resolucion_alto / 2) - (self.frameSize().height()/2) 
        self.move(left, top)
    
        #Asignar un tipo de fuente 
        qfont = QFont("Arial",10,QFont.Bold)
        self.setFont(qfont)
             
        #valor_boton = self.boton_2.text()
        
        self.boton_0.clicked.connect(lambda: self.update_label("0"))
        self.boton_1.clicked.connect(lambda: self.update_label("1"))
        self.boton_2.clicked.connect(lambda: self.update_label("2"))
        self.boton_3.clicked.connect(lambda: self.update_label("3"))
        self.boton_4.clicked.connect(lambda: self.update_label("4"))
        self.boton_5.clicked.connect(lambda: self.update_label("5"))
        self.boton_6.clicked.connect(lambda: self.update_label("6"))
        self.boton_7.clicked.connect(lambda: self.update_label("7"))
        self.boton_8.clicked.connect(lambda: self.update_label("8"))
        self.boton_9.clicked.connect(lambda: self.update_label("9"))
        self.btn_punto_dec.clicked.connect(lambda: self.update_label("."))
        self.btn_limpiar.clicked.connect(lambda: self.numero.setText(""))
        
        self.btn_5_porc.clicked.connect(lambda: self.calculo_5_porc())
        self.btn_10_porc.clicked.connect(lambda: self.calculo_10_porc())
        self.btn_15_porc.clicked.connect(lambda: self.calculo_15_porc())
        self.btn_20_porc.clicked.connect(lambda: self.calculo_20_porc())
        
        self.numero.setText("")
        

    def showEvent(self, event):
        self.bienvenido.setText("Bienvenido!!")

    def closeEvent(self, event):
        resultado = QMessageBox.question(self, "Salir", "¿Seguro que quieres salir de la aplicación?",
                                        QMessageBox.Yes  | QMessageBox.No)
        if resultado == QMessageBox.Yes: event.accept()
        else: event.ignore()
        
    def update_label(self, _str):
        self.numero.setText(self.numero.text() + _str)
        
    def calculo_5_porc(self):
        numero_a_evaluar = float(self.numero.text())
        propina = numero_a_evaluar * 0.05
        self.numero.setText(repr(propina))
        
    def calculo_10_porc(self):
        numero_a_evaluar = float(self.numero.text())
        propina = numero_a_evaluar * 0.10
        self.numero.setText(repr(propina))
        
    def calculo_15_porc(self):
        numero_a_evaluar = float(self.numero.text())
        propina = numero_a_evaluar * 0.15
        self.numero.setText(repr(propina))
        
    def calculo_20_porc(self):
        numero_a_evaluar = float(self.numero.text())
        propina = numero_a_evaluar * 0.20
        self.numero.setText(repr(propina))
        
#Instancia para iniciar una aplicacion
app = QApplication(sys.argv) 

#Crear un objeto de clase 
_ventana = Ventana()

#Mostrar las ventana
_ventana.show()

#Ejecutar la aplicacion 
app.exec()
