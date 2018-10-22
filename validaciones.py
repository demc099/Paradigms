#Validar
import re

import funcionesAlgoritmo
import inoutFile
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMessageBox, QDialog, QWidget,
                               QGroupBox, QGridLayout, QVBoxLayout, QLineEdit, QPushButton, QLabel, QInputDialog)


"""Este método revisa si los campos de simbolos, variables y marcadores están vacíos y si lo están agrega valores por defecto, siempre y cuando las reglas se hayan insertado
las reglas"""
def camposBlancos(self):
  symbols = self.symbolsEdit.text()
  vars = self.varsEdit.text()
  markers = self.markersEdit.text()
  grammar = self.grammarEdit.toPlainText()
  if (symbols== "" and vars== "" and markers=="" and grammar!= ""):
      self.symbolsEdit.setText("abcdefghijklmnopqrstuvwxyz0123456789")
      self.symbolsEdit.setStyleSheet("color: blue; border: 1px solid yellow;")
      self.varsEdit.setText("wxyz")
      self.varsEdit.setStyleSheet("color: blue; border: 1px solid yellow;")
      self.markersEdit.setText("αβγδ")
      self.markersEdit.setStyleSheet("color: blue; border: 1px solid yellow;")


"""Este método verifica que los simbolos se hayan ingresado correctamente; que sean letras, números u otros carateres especiales"""
def validarSim(self):
  symbols= self.symbolsEdit.text()
  validar = re.match('^[\w\(\)\[\]\*\+\,\¿\?\!\#\¡\$\&\%\{\}]+$', symbols, re.I)
  if not validar:
   self.symbolsEdit.setStyleSheet("color: blue; border: 1px solid red;")
   return False
  else:
   self.symbolsEdit.setStyleSheet("color: blue; border: 1px solid green;")
   return True


"""Este método verifica que las variables se hayan ingresado correctamente; que sean letras, números u otros carateres especiales"""
def validarVars(self):
  vars = self.varsEdit.text()
  validar = re.match('^[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}]+$', vars, re.I)
  if not validar:
   self.varsEdit.setStyleSheet("color: blue; border: 1px solid red;")
   return False
  else:
   self.varsEdit.setStyleSheet("color: blue; border: 1px solid green;")
   return True


"""Este método verifica que los marcadores se hayan ingresado correctamente; que sean letras, números o letras del alfabeto griego"""
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


"""Este método verifica que los marcadores no tengan los mismos caracteres que los simbolos ni las variables"""
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
   #print('No hay')
   return True


""""Este método verifica que las reglas ingresadas cumplan con lo siguiente:
1) Que cada una de las reglas cumpla con un patron dado (por ejemplo tiene que ir a -> b es decir, espacios entre flecha
2) Que cada caracter ingresado se encuentre en simbolos, variables o marcadores (debe estar en al menos 1) """
def validarGramatica(self):
  listaSim = list(self.symbolsEdit.text())
  listaVar = list(self.varsEdit.text())
  listaMar = list(self.markersEdit.text())
  lineas = str(self.grammarEdit.toPlainText()).split('\n')
  for linea in lineas:
      #patron1 = re.compile('^(\"[\w\(\)\[\]\*\+\,\¿\?\!\#\¡\$\&\%\{\}\s]+\"|[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}]+)\s\-\>\s(\"[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}\s]+\"|[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}]+)\.?$')
      patron1 = re.compile('^(\"[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}\s]+\"|[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}]+)\s\-\>\s(\"[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}\s]+\"|[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}]+)\.?$')
      patron2 = re.compile('^%[\w\s]+')
      if (linea != "" and  not patron2.match(linea)):
        if (patron1.match(linea)):
            for carac in linea:
                if (carac != "-" and carac != ">" and carac != '"' and carac !=" " and carac != "." and carac != "Λ"):
                    sym = [item for item in listaSim if carac in listaSim]
                    var = [item for item in listaVar if carac in listaVar]
                    mar = [item for item in listaMar if carac in listaMar]
                    if (len(sym) == 0 and len(var) == 0 and len(mar) == 0):
                       self.grammarEdit.setStyleSheet("color: blue; border: 1px solid red;")
                       bandera = False
                       break
                    else:
                       bandera = True
        else:
            self.grammarEdit.setStyleSheet("color: blue; border: 1px solid red;")
            bandera = False
            break


  return bandera


""""Este método sirve para enviar un mensaje de error al usuario"""
def enviarMensError(self, msj):
    ret = QMessageBox.critical(self, "Error",msj, QMessageBox.Ok)


"""Este método se asegura que los simbolos, las variables, los marcadores y las reglas cumplan con el formato correcto para luego poder llamar al método guardar o
 correr el algoritmo sin temor a que hayan errores en estos y no funcione adecuadamente la resolución o que se guarde algo no permitido"""
def conjuntodevalidacionesdePrueba(self):
    camposBlancos(self)
    if validarSim(self) == True and validarVars(self) == True and validarMark(self) == True:
        if validarIgualdad(self) == True:
            if self.grammarEdit.toPlainText() == "":
                enviarMensError(self, "No hay reglas de producción")
            else:
                if validarGramatica(self) == True:
                    self.grammarEdit.setStyleSheet("color: blue; border: 1px solid green;")
                    #funcionesAlgoritmo.correrAlgoritmo(self)
                    return True
                else:
                    enviarMensError(self, "Asegurese de escribir correctamente las reglas")
        else:
            enviarMensError(self, "Verifique que los marcadores ingresados no coincidan con los simbolos ni las variables ingresadas")
    else:
        enviarMensError(self, "Por favor ingrese los caracteres correctamente e inténtelo de nuevo!")
