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
    file.write(self.grammarEdit.toPlainText()+ "\n")
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
        patronSym = re.search('^\#symbols\s[a-z0-9]+', line, re.UNICODE)
        patronVars = re.search('^\#vars\s[\w]+', line, re.UNICODE)
        patronMark = re.search('^\#markers\s[\w]+', line, re.UNICODE)
        patronRules = re.search('^[\w+\-\>\w+]', line, re.UNICODE)
        print(patronSym)
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
    file.close()
    

def cargarXml(self, fileName):
    file = open(fileName, 'r', encoding='utf-8')
    lines = file.readlines()
    self.grammarEdit.setText("")
    for line in lines:
        patronSym = re.search('^\<symbols\>[a-z0-9]+\<\/symbols\>', line, re.UNICODE)
        patronVars = re.search('^\<vars\>[\w]+\<\/vars\>', line, re.UNICODE)
        patronMark = re.search('^\<markers\>[\w]+\<\/markers\>', line, re.UNICODE)
        patronRules = re.search('^\<rules\>[\w+\s\-\>]+\<\/rules\>', line,re.UNICODE)
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
            pr = pr4.replace("</rules>","")
            self.grammarEdit.setText(self.grammarEdit.toPlainText()+pr4.replace("</rules>",""))
    file.close()
