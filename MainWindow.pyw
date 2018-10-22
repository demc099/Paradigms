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

#clase de la ventana principal
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
  self.grammarEdit.setText("")

  #Poner imagenes a los botones
  self.clearRegistryButton.setIcon(QIcon('image/cancelar.png'))
  self.clearFileButton.setIcon(QIcon('image/cancelar.png'))
  self.clearButton.setIcon(QIcon('image/cancelar.png'))
  self.saveButton.setIcon(QIcon('image/guardar.png'))
  self.runButton.setIcon(QIcon('image/run.png'))
  self.nextButton.setIcon(QIcon('image/siguiente.png'))
  self.saveFileButton.setIcon(QIcon('image/guardar.png'))
  self.saveRegistryButton.setIcon(QIcon('image/guardar.png'))

  #Creacion del menu de la ventana
  menu= self.menuBar()
  menuArchivo = menu.addMenu("Archivo")
  menuHerramientas = menu.addMenu("Herramientas")
  menuPrueba = menu.addMenu("Algoritmos de prueba")

  #Agregar elementos a los menus principales
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
  menuA_guardar.triggered.connect(self.conjuntodevalidaciones)
  menuH_cargarArchivo.triggered.connect(self.cargarPrueba)
  menuP_1.triggered.connect(lambda:self.cargarAlgoritmoX("Invertir una hilera"))
  menuP_2.triggered.connect(lambda: self.cargarAlgoritmoX("Duplicar hilera"))
  menuP_3.triggered.connect(lambda: self.cargarAlgoritmoX("Palindromo"))
  menuP_4.triggered.connect(lambda: self.cargarAlgoritmoX("Binario a unario"))
  menuP_5.triggered.connect(lambda: self.cargarAlgoritmoX("Suma binarios"))
  menuP_6.triggered.connect(lambda: self.cargarAlgoritmoX("Triplicar binarios"))
  menuP_7.triggered.connect(lambda: self.cargarAlgoritmoX("Multiplicación binarios"))
  menuP_8.triggered.connect(lambda: self.cargarAlgoritmoX("Suma decimales"))
  menuP_9.triggered.connect(lambda: self.cargarAlgoritmoX("Eliminar caracteres repetidos consecutivos"))
  menuP_10.triggered.connect(lambda: self.cargarAlgoritmoX("Paréntesis balanceados"))

  #invocacion funciones para guardar
  self.saveButton.clicked.connect(self.conjuntodevalidaciones)
  self.saveFileButton.clicked.connect(self.guardarPrueba)
  self.saveRegistryButton.clicked.connect(self.guardarResultado)

  #invocacion funciones para el algoritmo
  self.runButton.clicked.connect(self.correrAlgoritmo)
  self.debugButton.clicked.connect(self.debug)
  self.nextButton.clicked.connect(self.contDebug)

  # Enable campos
  self.fileEdit.setEnabled(False)
  self.nextButton.setEnabled(False)
  self.clearFileButton.setEnabled(False)
  self.saveFileButton.setEnabled(False)
  self.clearRegistryButton.setEnabled(False)
  self.saveRegistryButton.setEnabled(False)

  #Input
  self.clearButton.clicked.connect(self.markersEdit.clear)
  self.clearButton.clicked.connect(self.varsEdit.clear)
  self.clearButton.clicked.connect(self.symbolsEdit.clear)
  self.clearButton.clicked.connect(self.grammarEdit.clear)
  self.clearButton.clicked.connect(self.lineEdit.clear)

  self.clearFileButton.clicked.connect(self.clearFileEdit)
  self.clearRegistryButton.clicked.connect(self.clearPrintText)


  #self.saveButton.clicked.connect(self.validar)
  self.symbolsEdit.textChanged.connect(self.validarSim)
  self.varsEdit.textChanged.connect(self.validarVars)
  self.markersEdit.textChanged.connect(self.validarMark)

  self.varQLineEdit = []


  
 #----------------------------------------------------------------------------------------------------------------

 #Funciones del menu
 def menuArchivoSalir(self):#si en el menu selecciona salir, cierra la ventana
     req = QMessageBox.question(self, "Mensaje", "Seguro quiere salir", QMessageBox.Yes, QMessageBox.No)
     if req == QMessageBox.Yes:
      sys.exit(app.exec_())

 def abrirPaleta(self):
     # Almacenaz el widget que tiene el focus
     self.varQLineEdit = QApplication.focusWidget()
     Caracteres(self).exec_()

# Declaración funcion Limpiar campos
 def clearFileEdit(self):
    self.fileEdit.setText("")
    self.lineEdit.setEnabled(True)
    self.fileEdit.setEnabled(False)
    self.clearFileButton.setEnabled(False)
    self.saveFileButton.setEnabled(False)

 def clearPrintText(self):
    self.printText.setText("")
    self.clearRegistryButton.setEnabled(False)
    self.saveRegistryButton.setEnabled(False)


# Declaración funciones guardar y cargar
 def guardar(self):
     inoutFile.guardar(self)

 def cargar(self):
     inoutFile.cargar(self)


# Declaración funciones guardar y cargar Pruebas
 def guardarPrueba(self):
  inoutFile.guardarPrueba(self)
  self.fileEdit.setText("")
  self.lineEdit.setEnabled(True)
  self.fileEdit.setEnabled(False)
  self.clearFileButton.setEnabled(False)
  self.saveFileButton.setEnabled(False)

 def guardarResultado(self):
  inoutFile.guardarResultado(self)

 def cargarPrueba(self):
  self.lineEdit.setEnabled(False)
  self.fileEdit.setEnabled(True)
  self.clearFileButton.setEnabled(True)
  self.saveFileButton.setEnabled(True)
  inoutFile.cargarPrueba(self)
  self.lineEdit.setText("")


 def cargarAlgoritmoX(self, nombre):
  nombre = "./algoritmos/"+nombre+".txt"
  inoutFile.cargarTxt(self, nombre)

# Declaración funciones algoritmo
 def aplicarAlgoritmo(self):
    linea= self.lineEdit.text()
    simbaceptados= self.symbolsEdit.text()
    variables= self.varsEdit.text()
    funcionesAlgoritmo.algoritmo(self, linea, variables)

 def debug(self):
  self.printText.clear()
  self.nextButton.setEnabled(True)
  self.deb = True
  self.cont = 1
  self.texto = self.lineEdit.text()
  funcionesAlgoritmo.debug(self, self.texto)

 def contDebug(self):
  self.deb = True
  self.cont = self.cont + 1
  funcionesAlgoritmo.debug(self, self.texto)

 
 def correrAlgoritmo(self):
  if self.lineEdit.isEnabled():
    validaciones.conjuntodevalidacionesdePrueba(self)
    #funcionesAlgoritmo.correrAlgoritmo(self)
  else:
    if self.fileEdit.isEnabled():
      funcionesAlgoritmo.correrAlgoritmoPruebas(self)


#Validar
 def validarSim(self):
  validaciones.validarSim(self)

 def validarVars(self):
  validaciones.validarVars(self)

 def validarMark(self):
  validaciones.validarMark(self)

 def validarGramatica(self):
  validaciones.validarGramatica(self)

 def conjuntodevalidaciones(self):
  validaciones.conjuntodevalidaciones(self)




 #-----------------------------------------------------------------------------------------------------------------

app = QApplication(sys.argv)
_ventana = Ventana()
_ventana.show()
sys.exit(app.exec_())
