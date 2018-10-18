from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import re

def guardar(self):
    fileName, _ = QFileDialog.getSaveFileName(self, "Guardar", "","Text Files (*.txt);;Xml Files (*.xml)")
    if fileName:
        validarFormatoGuardar(self, fileName)

def validarFormatoGuardar(self, fileName):
    patronTxt = re.match('^(\w):\/[(\w+\s?\w+)(áéíóúñ\_\#\-)+\/?]+\.txt$', fileName, re.I)
    patronXml = re.match('^(\w):\/[(\w+\s?\w+)(áéíóúñ\_\#\-)+\/?]+\.xml$', fileName, re.I)
    if (patronTxt):
        guardarTxt(self, fileName)
    if (patronXml):
        guardarXml(self, fileName)

def guardarTxt(self, fileName):
    file = open(fileName, "w", encoding='utf-8')
    file.write("#symbols "+self.symbolsEdit.text()+"\n")
    file.write("#vars "+self.varsEdit.text()+"\n")
    file.write("#markers "+self.markersEdit.text()+"\n")
    lines = str(self.grammarEdit.toPlainText()).split('\n')
    for line in lines:
        if (re.match("%[\w\s]+", line, re.I) or re.match("[\"?\w\s\"?]+\-\>[\"?\w\s\"?]", line, re.I)):
            file.write(line+ "\n")
    file.close()

def guardarXml(self, fileName):
    file = open(fileName, "w", encoding='utf-8')
    file.write("<?xml version='1.0' encoding='UTF-8'?>"+"\n")
    file.write("<algoritmo>"+"\n")
    file.write("<symbols>"+self.symbolsEdit.text()+"</symbols>"+"\n")
    file.write("<vars>"+self.varsEdit.text()+"</vars>"+"\n")
    file.write("<markers>"+self.markersEdit.text() + "</markers>"+"\n")
    lines = str(self.grammarEdit.toPlainText()).split('\n')
    for line in lines:
        if re.match("%[\w\s]+", line, re.I):
            file.write("<comment>"+line+"</comment>"+"\n")
        if re.match("[\"?\w\s\"?]+\-\>[\"?\w\s\"?]", line, re.I):
            file.write("<rules>"+line+"</rules>"+"\n")
    file.write('</algoritmo>')

def cargar(self):
    fileName, _ = QFileDialog.getOpenFileName(self, "Abrir como", "","Text Files (*.txt);;Xml Files (*.xml)")
    if fileName:
        validarFormatoCargar(self, fileName)

def validarFormatoCargar(self, fileName):
    patronTxt = re.match('^(\w):\/[(\w+\s?\w+)(áéíóúñ\_\#\-)+\/?]+\.txt$', fileName, re.I)
    patronXml = re.match('^(\w):\/[(\w+\s?\w+)(áéíóúñ\_\#\-)+\/?]+\.xml$', fileName, re.I)
    if(patronTxt):
        cargarTxt(self, fileName)
    if(patronXml):
        cargarXml(self, fileName)

def cargarTxt(self, fileName):
    file = open(fileName, 'r', encoding='utf-8')
    lines = file.readlines()
    self.grammarEdit.setText("")
    for line in lines:
        #patronSym = re.search('^\#symbols\s[a-z0-9]+', line, re.I)
        patronSym = re.search('^\#symbols\s[a-z0-9]+', line, re.UNICODE)
        patronVars = re.search('^\#vars\s[a-zA-Z0-9áéíóúàèìòùäëïöü]+', line, re.UNICODE)
        patronMark = re.search('^\#markers\s[a-zA-Z0-9áéíóúàèìòùäëïöüαβγδεζηθικλμνξοπρσςτυφχψωΛ]+', line, re.UNICODE)
        patronRules = re.search('^[\"?\w+\"?\-\>\"?\w+\"?]', line, re.UNICODE)
        #patronRules = re.search('^[\w+\-\>\w+]', line, re.UNICODE)
        patronComment = re.search('^%[\w\s]+', line, re.UNICODE)

        if patronSym:
            pr = line.replace("#symbols ","")
            self.symbolsEdit.setText(pr.rstrip())
        if patronVars:
            pr = line.replace("#vars ","")
            self.varsEdit.setText(pr.rstrip())
        if patronMark:
            pr = line.replace("#markers ","")
            self.markersEdit.setText(pr.rstrip())
        if patronRules:
            self.grammarEdit.setText(self.grammarEdit.toPlainText()+line)
        if patronComment:
            self.grammarEdit.setText(self.grammarEdit.toPlainText()+line)
    file.close()
    

def cargarXml(self, fileName):
    file = open(fileName, 'r', encoding='utf-8')
    lines = file.readlines()
    self.grammarEdit.setText("")
    for line in lines:
        patronSym = re.search('^\<symbols\>[a-z0-9áéíóúàèìòùäëïöü]+\<\/symbols\>', line, re.UNICODE)
        patronVars = re.search('^\<vars\>[a-zA-Z0-9áéíóúàèìòùäëïöü]+\<\/vars\>', line, re.UNICODE)
        patronMark = re.search('^\<markers\>[a-zA-Z0-9áéíóúàèìòùäëïöüαβγδεζηθικλμνξοπρσςτυφχψωΛ]+\<\/markers\>', line, re.UNICODE)
        patronRules = re.search('^\<rules\>[\"?\w\s\"?]+\-\>[\"?\w\s\"?]+\<\/rules\>', line,re.UNICODE)
        patronComment = re.search('^\<comment\>%[\w\s]+\<\/comment\>', line, re.UNICODE)
        if patronSym:
            pr1 = line.replace("<symbols>","")
            pr = pr1.replace("</symbols>","")
            self.symbolsEdit.setText(pr.rstrip())
        if patronVars:
            pr2 = line.replace("<vars>","")
            pr = pr2.replace("</vars>","")
            self.varsEdit.setText(pr.rstrip())
        if patronMark:
            pr3 = line.replace("<markers>","")
            pr = pr3.replace("</markers>","")
            self.markersEdit.setText(pr.rstrip())
        if patronRules:
            pr4 = line.replace("<rules>","")
            self.grammarEdit.setText(self.grammarEdit.toPlainText()+pr4.replace("</rules>",""))
        if patronComment:
            pr5 = line.replace("<comment>","")
            self.grammarEdit.setText(self.grammarEdit.toPlainText() + pr5.replace("</comment>", ""))
    file.close()


#-------------------- Funciones Cargar y  Guardar Archivo de Pruebas --------------------
def guardarPrueba(self):
    fileNamePrueba, _ = QFileDialog.getSaveFileName(self, "Guardar", "","Text Files (*.txt)")
    if fileNamePrueba:
        validarGuardarPrueba(self, fileNamePrueba)

def validarGuardarPrueba(self, fileNamePrueba):
    patronTxtPrueba = re.match('^(\w):\/[(\w+\s?\w+)(áéíóúñ\_\#\-)+\/?]+\.txt$', fileNamePrueba, re.I)
    if (patronTxtPrueba):
        guardarTxtPrueba(self, fileNamePrueba)


def guardarTxtPrueba(self, fileNamePrueba):
    file = open(fileNamePrueba, "w", encoding='utf-8')
    file.write(self.fileEdit.toPlainText()+ "\n")
    file.close()



def cargarPrueba(self):
    fileNamePrueba, _ = QFileDialog.getOpenFileName(self, "Abrir Documento de Pruebas", "","Text Files (*.txt)")
    if fileNamePrueba:
        validarCargarPrueba(self, fileNamePrueba)

def validarCargarPrueba(self, fileNamePrueba):
    patronTxtPrueba = re.match('^(\w):\/[(\w+\s?\w+)(áéíóúñ\_\#\-)+\/?]+\.txt$', fileNamePrueba, re.I)
    if(patronTxtPrueba):
        cargarTxtPrueba(self, fileNamePrueba)

def cargarTxtPrueba(self, fileNamePrueba):
    filePrueba = open(fileNamePrueba, 'r', encoding='utf-8')
    linesPrueba = filePrueba.readlines()

    self.fileEdit.setText("")

    for linePrueba in linesPrueba:
        patronPrueba = re.search('^[\w]+', linePrueba, re.UNICODE)
        if patronPrueba:
            self.fileEdit.setText(self.fileEdit.toPlainText()+linePrueba.replace(' ', ''))
    filePrueba.close()
    
