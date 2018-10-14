#Validar
import re


def validarSim(self):
  symbols= self.symbolsEdit.text()
  validar = re.match('^[a-z\sáéíóúàèìòùäëïöü]+$', symbols, re.I)
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
  validar = re.match('^[a-z\sáéíóúàèìòùäëïöü]+$', vars, re.I)
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
  validar = re.match('^[a-z\sáéíóúàèìòùäëïöüαβγδ]+$', markers, re.I)
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
  print(listaSim)
  print(listaVar)
  print(listaMar)
  comparacion = [item for item in listaSim if item in listaMar]
  if len(comparacion) > 0:
   for item in comparacion:

    print('I=> '+ '%s' % item)
    self.markersEdit.setStyleSheet("color: blue; border: 1px solid red;")
    return False
  else:
   print('No hay')
   return True

def validarGramatica(self):
  texto1= self.grammarEdit.toPlainText()
  print(texto1)
  linea = str(self.grammarEdit.toPlainText()).split('\n')
  print(linea)
  nuevaLinea= busqueda(linea)
  print(nuevaLinea)
  #print(len(linea))
  #print(linea[0])

def busqueda(linea):
  caracter ='->'
  cont=0
  i = 0
  while i < len(linea):
   dato=linea[i]
   print(dato)
   if caracter in dato:
    posflecha=dato.index(caracter)
    if posflecha == 0 or posflecha == len(dato)-1:
     print(posflecha)
     cont+=1
   else:
    print("Linea errornea")
   i += 1
  if cont == len(linea)-1:
   print(cont)
   return True
  else:
   print(cont)
   return False