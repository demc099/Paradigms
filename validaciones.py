#Validar
import re
import inoutFile
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMessageBox, QDialog, QWidget,
                               QGroupBox, QGridLayout, QVBoxLayout, QLineEdit, QPushButton, QLabel, QInputDialog)

def camposBlancos(self):
  symbols = self.symbolsEdit.text()
  vars = self.varsEdit.text()
  markers = self.markersEdit.text()
  if symbols.isspace:
    self.symbolsEdit.setText("abcdefghijklmnopqrstuvwxyz0123456789")
    self.symbolsEdit.setStyleSheet("color: blue; border: 1px solid yellow;")
  if vars.isspace:
    self.varsEdit.setText("wxyz")
    self.varsEdit.setStyleSheet("color: blue; border: 1px solid yellow;")
  if markers.isspace:
    self.markersEdit.setText("αβγδ")
    self.markersEdit.setStyleSheet("color: blue; border: 1px solid yellow;")


def validarSim(self):
  symbols= self.symbolsEdit.text()
  validar = re.match('^[a-z0-9áéíóúàèìòùäëïöü]+$', symbols, re.I)
  if not validar:
   self.symbolsEdit.setStyleSheet("color: blue; border: 1px solid red;")
   return False
  else:
   self.symbolsEdit.setStyleSheet("color: blue; border: 1px solid green;")
   return True


def validarVars(self):
  vars = self.varsEdit.text()
  validar = re.match('^[a-z0-9\sáéíóúàèìòùäëïöü]+$', vars, re.I)
  if not validar:
   self.varsEdit.setStyleSheet("color: blue; border: 1px solid red;")
   return False
  else:
   self.varsEdit.setStyleSheet("color: blue; border: 1px solid green;")
   return True


def validarMark(self):
  markers = self.markersEdit.text()
  validar = re.match('^[a-z0-9\sáéíóúàèìòùäëïöüαβγδεζηθικλμνξοπρσςτυφχψωΛ]+$', markers, re.I)
  if not validar:
    validar = re.match('^[a-z0-9áéíóúàèìòùäëïöüαβγδεζηθικλμνξοπρσςτυφχψω]+$', markers, re.I)
  if markers == "   ":
   self.markersEdit.setText("αβγδ")
   self.markersEdit.setStyleSheet("color: blue; border: 1px solid yellow;")
   return True
  elif not validar:
   self.markersEdit.setStyleSheet("color: blue; border: 1px solid red;")
   return False
  else:
   self.markersEdit.setStyleSheet("color: blue; border: 1px solid green;")
   return True



def validarIgualdad(self):
  listaSim= list(self.symbolsEdit.text())
  listaVar = list(self.varsEdit.text())
  listaMar = list(self.markersEdit.text())
  compSym = [item for item in listaMar if item in listaSim]
  compVar = [item for item in listaMar if item in listaVar]
  if len(compSym) > 0:
      for item in compSym:
          #print('I=> '+ '%s' % item + "se metio al primero")
          self.markersEdit.setStyleSheet("color: blue; border: 1px solid red;")
      return False
  elif len(compVar) > 0:
      for item in compVar:
          #print('I=> ' + '%s' % item + "se metio al segundo")
          self.markersEdit.setStyleSheet("color: blue; border: 1px solid red;")
      return False
  else:
   print('No hay')
   return True


def validarGramatica(self):
  listaSim = list(self.symbolsEdit.text())
  listaVar = list(self.varsEdit.text())
  listaMar = list(self.markersEdit.text())
  rules = self.grammarEdit.toPlainText()
  lineas = str(self.grammarEdit.toPlainText()).split('\n')
  for linea in lineas:
    for carac in linea:
        if (carac != "-" and carac != ">"):
            print(carac)


def busqueda(linea):
  caracter ='->'
  i = 0
  while i < len(linea):
      dato=linea[i]
      print(dato)
      if caracter in dato:
          posflecha=dato.index(caracter)
          print (posflecha)
          #pos=posicion(dato,posflecha)
      #elif pos == False:
        #print("Existe datos erroneos")

      else:
          print("Linea errornea")
          i += 1


def enviarMensError(self, msj):
    ret = QMessageBox.critical(self, "Error",msj, QMessageBox.Ok)

def conjuntodevalidaciones(self):
    camposBlancos(self)
    if validarSim(self) == True and validarVars(self) == True and validarMark(self) == True:
        validarGramatica(self)
        if validarIgualdad(self) == True:
            #if validarGramatica(self) == True:
            self.grammarEdit.setStyleSheet("color: blue; border: 1px solid green;")
            inoutFile.guardar(self)
        else:
            enviarMensError(self, "Verifique que los marcadores ingresados no coincidan con los simbolos ni las variables ingresadas")
    else:
        enviarMensError(self, "Usted a ingresado caracteres no permitidos, por favor ingreselos correctamente e inténtelo de nuevo!")
