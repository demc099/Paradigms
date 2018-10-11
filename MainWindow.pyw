import sys

from PyQt5.QtGui import QIcon, QPixmap, QStandardItemModel
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMessageBox, QDialog, QWidget,
                               QGroupBox, QGridLayout, QVBoxLayout, QLineEdit, QPushButton, QLabel, QInputDialog)
from PyQt5 import uic

from paletaCaracteres import *
import funcionesAlgoritmo
import inoutFile


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

 # #Enable campos
 #  self.symbolsEdit.setEnabled(False)
 #  self.varsEdit.setEnabled(False)
 #  self.markersEdit.setEnabled(False)
 #  self.tableWidget.setEnabled(False)
 #  self.saveButton.setEnabled(False)
 #  self.clearButton.setEnabled(False)
 #  self.putButton.setEnabled(False)
 #  self.removeButton.setEnabled(False)

  #----------------------------------------------------------------------------------------------------------------
  #invocacion funciones para el menu
  menuA_salir.triggered.connect(self.menuArchivoSalir)
  menuH_paleta.triggered.connect(self.abrirPaleta)

  #invocacion funciones para guardar y cargar
  self.saveButton.clicked.connect(self.guardarTxt)

  #invocacion funciones para el algoritmo
  self.runButton.clicked.connect(self.aplicarAlgoritmo)

  #Input
  self.clearButton.clicked.connect(self.markersEdit.clear)
  self.clearButton.clicked.connect(self.varsEdit.clear)
  self.clearButton.clicked.connect(self.symbolsEdit.clear)
  self.clearButton.clicked.connect(self.grammarEdit.clear)

 #----------------------------------------------------------------------------------------------------------------

 #Funciones del menu
 def menuArchivoSalir(self):
     QMessageBox.question(self, "Mensaje", "Seguro quiere salir", QMessageBox.Yes, QMessageBox.No)


 def abrirPaleta(self):
     Caracteres(self).exec_()


# Declaración funciones guardar y cargar
 def guardarTxt(self):
     inoutFile.guardarTxt(self)


# Declaración funciones algoritmo
 def aplicarAlgoritmo(self):
    linea= self.lineEdit.text()
    funcionesAlgoritmo.algoritmo(self, linea)



#-----------------------------------------------------------------------------------------------------------------



app = QApplication(sys.argv)
_ventana = Ventana()
_ventana.show()
app.exec_()
