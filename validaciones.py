#Validar
import re
import inoutFile
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMessageBox, QDialog, QWidget,
                               QGroupBox, QGridLayout, QVBoxLayout, QLineEdit, QPushButton, QLabel, QInputDialog)


def validarSim(self):
  symbols= self.symbolsEdit.text()
  validar = re.match('^[a-z0-9áéíóúàèìòùäëïöü]+$', symbols, re.I)
  if symbols == "   ":
   self.symbolsEdit.setText("abcdefghijklmnopqrstuvwxyz0123456789")
   self.symbolsEdit.setStyleSheet("color: blue; border: 1px solid yellow;")
   return True
  elif not validar:
   self.symbolsEdit.setStyleSheet("color: blue; border: 1px solid red;")
   return False
  else:
   self.symbolsEdit.setStyleSheet("color: blue; border: 1px solid green;")
   return True

def validarVars(self):
  vars = self.varsEdit.text()
  validar = re.match('^[a-z0-9áéíóúàèìòùäëïöü]+$', vars, re.I)
  if vars == "   ":
   self.varsEdit.setText("wxyz")
   self.varsEdit.setStyleSheet("color: blue; border: 1px solid yellow;")
   return True
  elif not validar:
   self.varsEdit.setStyleSheet("color: blue; border: 1px solid red;")
   return False
  else:
   self.varsEdit.setStyleSheet("color: blue; border: 1px solid green;")
   return True

def validarMark(self):
  markers = self.markersEdit.text()
  validar = re.match('^[a-z0-9áéíóúàèìòùäëïöüαβγδεζηθικλμνξοπρσςτυφχψωΛ]+$', markers, re.I)
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

  #3790

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
  #print(texto1)
  lineas = str(self.grammarEdit.toPlainText()).split('\n')
  for linea in lineas:
      for carac in linea:
          if (carac != "-" and carac != ">"):
              print(carac)



  #print(linea)
  #nuevaLinea= busqueda(linea)
  #return nuevaLinea
  #print(len(linea))
  #print(linea[0])

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

# def posicion(dato,posflecha):
#     if posflecha == 0 or posflecha == len(dato) - 1:
#         print(posflecha)
#         return False
#     else:
#         return True
#
#     if cont == len(linea)-1:
#       print(cont)
#       if bool == True:
#           return True
#       else:
#           print(cont)
#           return False

def enviarMensError(self, msj):
    ret = QMessageBox.critical(self, "Error",msj, QMessageBox.Ok)

def conjuntodevalidaciones(self):
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
