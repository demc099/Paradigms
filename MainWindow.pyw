import re
import sys

from PyQt5.QtGui import QIcon, QPixmap, QStandardItemModel
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMessageBox, QDialog, QWidget,
                               QGroupBox, QGridLayout, QVBoxLayout, QLineEdit, QPushButton, QLabel, QInputDialog)
from PyQt5 import uic

from paletaCaracteres import *
import funcionesAlgoritmo
import inoutFile
import validaciones


class Ventana(QMainWindow):   
 def __init__(self):
  QMainWindow.__init__(self)
  uic.loadUi("MainWindowInterfaz.ui", self)
  self.setWindowTitle("Traductor")
  self.setWindowIcon(QIcon('image/compiler.png'))

  #Datos default
  self.symbolsEdit.setText("abcdefghijklmnopqrstuvwxyz0123456789")
  self.varsEdit.setText("wxyz")
  self.markersEdit.setText("αβγδ")

  #Poner imagenes a los botones
  self.clearButton.setIcon(QIcon('image/cancelar.png'))
  self.saveButton.setIcon(QIcon('image/guardar.png'))
  self.runButton.setIcon(QIcon('image/run.png'))
  self.nextButton.setIcon(QIcon('image/siguiente.png'))

  #Creacion del menu de la ventana
  menu= self.menuBar()
  menuArchivo = menu.addMenu("Archivo")
  menuHerramientas = menu.addMenu("Herramientas")
  menuPrueba = menu.addMenu("Algoritmos de prueba")

  #Agregar elementos a los menus principales
  menuA_nuevo = QAction(QIcon(),"Nuevo",self)
  menuArchivo.addAction(menuA_nuevo)

  menuA_abrir = QAction(QIcon(), "Abrir", self)
  menuA_abrir.setShortcut("Ctrl+a")
  menuArchivo.addAction(menuA_abrir)

  menuA_guardar = QAction(QIcon(), "Guardar", self)
  menuArchivo.addAction(menuA_guardar)

  menuA_salir = QAction(QIcon(), "Salir", self)
  menuArchivo.addAction(menuA_salir)

  menuH_paleta = QAction(QIcon(), "Paleta de caracteres", self)
  menuH_paleta.setShortcut("Ctrl+p")
  menuH_paleta.setStatusTip("Abrir la paleta de caracteres")
  menuHerramientas.addAction(menuH_paleta)

  menuH_cargarArchivo = QAction(QIcon(), "Cargar archivo de prueba", self)
  menuHerramientas.addAction(menuH_cargarArchivo)


  menuP_1 = QAction(QIcon(), "Invertir una hilera", self)
  menuPrueba.addAction(menuP_1)
  menuP_2 = QAction(QIcon(), "Duplicar hilera", self)
  menuPrueba.addAction(menuP_2)
  menuP_3 = QAction(QIcon(), "Palindromo", self)
  menuPrueba.addAction(menuP_3)
  menuP_4 = QAction(QIcon(), "Binario a unario", self)
  menuPrueba.addAction(menuP_4)
  menuP_5 = QAction(QIcon(), "Suma binarios", self)
  menuPrueba.addAction(menuP_5)
  menuP_6 = QAction(QIcon(), "Triplicar binarios", self)
  menuPrueba.addAction(menuP_6)
  menuP_7 = QAction(QIcon(), "Multiplicación binarios", self)
  menuPrueba.addAction(menuP_7)
  menuP_8 = QAction(QIcon(), "Suma decimales", self)
  menuPrueba.addAction(menuP_8)
  menuP_9 = QAction(QIcon(), "Eliminar caracteres repetidos consecutivos", self)
  menuPrueba.addAction(menuP_9)
  menuP_10 = QAction(QIcon(), "Paréntesis balanceados", self)
  menuPrueba.addAction(menuP_10)



  #----------------------------------------------------------------------------------------------------------------
  #invocacion funciones para el menu
  menuA_salir.triggered.connect(self.menuArchivoSalir)
  menuH_paleta.triggered.connect(self.abrirPaleta)
  menuA_abrir.triggered.connect(self.cargar)

  #invocacion funciones para guardar
  self.saveButton.clicked.connect(self.guardar)

  #invocacion funciones para guardar y cargar
  #self.saveButton.clicked.connect(self.guardarTxt)
  self.saveButton.clicked.connect(self.conjuntodevalidaciones)

  #invocacion funciones para el algoritmo
  self.runButton.clicked.connect(self.correrAlgoritmo)

  # Enable campos
  self.ruleLabel.setEnabled(False)
  self.afterLabel.setEnabled(False)
  self.beforeLabel.setEnabled(False)
  self.ruleEdit.setEnabled(False)
  self.afterEdit.setEnabled(False)
  self.beforeEdit.setEnabled(False)
  self.nextButton.setEnabled(False)

  #Input
  self.clearButton.clicked.connect(self.markersEdit.clear)
  self.clearButton.clicked.connect(self.varsEdit.clear)
  self.clearButton.clicked.connect(self.symbolsEdit.clear)
  self.clearButton.clicked.connect(self.grammarEdit.clear)

  #self.saveButton.clicked.connect(self.validar)
  self.symbolsEdit.textChanged.connect(self.validarSim)
  self.varsEdit.textChanged.connect(self.validarVars)
  self.markersEdit.textChanged.connect(self.validarMark)

  #output
  self.debugButton.clicked.connect(self.habilitarDebug)

  #Ventana Hija "Caraacteres"
  self.children = []
 #----------------------------------------------------------------------------------------------------------------

 #Funciones del menu
 def menuArchivoSalir(self):
     QMessageBox.question(self, "Mensaje", "Seguro quiere salir", QMessageBox.Yes, QMessageBox.No)


 def abrirPaleta(self):

    # wfocus = focusWidget() # supuestamente esto manda el nombre del widget que tiene el focus pero no me funciona se cae"
    # Si funciona se lo paso por parametros a la clase caracteres.
    
    
     child = Caracteres(self)
     self.children.append(child)


# Declaración funciones guardar y cargar
 def guardar(self):
     inoutFile.guardar(self)

 def cargar(self):
     inoutFile.cargar(self)


# Declaración funciones algoritmo
 def aplicarAlgoritmo(self):
    linea= self.lineEdit.text()
    simbaceptados= self.symbolsEdit.text()
    variables= self.varsEdit.text()
    funcionesAlgoritmo.algoritmo(self, linea, variables)

 def correrAlgoritmo(self):
  funcionesAlgoritmo.correrAlgoritmo(self)

#Debug
 def habilitarDebug(self):
  self.ruleLabel.setEnabled(True)
  self.afterLabel.setEnabled(True)
  self.beforeLabel.setEnabled(True)
  self.ruleEdit.setEnabled(True)
  self.afterEdit.setEnabled(True)
  self.beforeEdit.setEnabled(True)
  self.nextButton.setEnabled(True)

#Validar
 def validarSim(self):
  validaciones.validarSim(self)

 def validarVars(self):
  validaciones.validarVars(self)

 def validarMark(self):
  validaciones.validarMark(self)

 def validarIgualdad(self):
  validaciones.validarIgualdad(self)

 def validarGramatica(self):
  validaciones.validarGramatica(self)

 def busqueda(self,linea):
  validaciones.busqueda(self)

 def conjuntodevalidaciones(self):
  validaciones.conjuntodevalidaciones(self)


 #-----------------------------------------------------------------------------------------------------------------

app = QApplication(sys.argv)
_ventana = Ventana()
_ventana.show()
app.exec_()
