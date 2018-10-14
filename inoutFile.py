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
    file.write("<markers>"+self.markersEdit.text() + "</markers>" + "\n")
    lines = str(self.grammarEdit.toPlainText()).split('\n')
    num = len(lines)
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
    text = file.read()
    self.printText.setText(text)
    file.close()

def cargarXml(self, fileName):
    file = open(fileName, 'r', encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        #patronSym = re.match('^\<symbols\>[a-z0-9]+\<\/symbols\>', line, re.I)
        patronSym = re.search('^\<symbols\>[a-z0-9]+\<\/symbols\>', line, re.I)
        patronVars = re.search('^\<vars\>[a-z]+\<\/vars\>', line, re.I)
        patronMark = re.match('^\<markers\>[α|β|γ|δ|ε|ζ|η|θ|ι|κ|λ|μ|ν|ξ|ο|π|ρ|σ|τ|ς|τ|υ|φ|χ|ψ|ω|Λ]+\<\/markers\>', line, re.UNICODE)
        patronRules = re.match('^\<rules\>[\w|\-\>]+\<\/rules\>', line, re.I)
        if patronSym:
            objSym = re.search('[^\<symbols\>][a-z0-9]+', patronSym.group(), re.I)
            if objSym:
                self.symbolsEdit.setText(objSym.group())
        if patronVars:
            objVar = re.search('[^\<vars\>][a-z]+', patronVars.group(), re.I)
            if objVar:
                self.varsEdit.setText(objVar.group())
        if patronMark:
            objMark = re.search('[^\<markers\>][α|β|γ|δ|ε|ζ|η|θ|ι|κ|λ|μ|ν|ξ|ο|π|ρ|σ|τ|ς|τ|υ|φ|χ|ψ|ω|Λ]+', patronMark.group(), re.I)
            if objMark:
                self.markersEdit.setText(objMark.group())
        if patronRules:
            objRul = re.search('[^\<rules\>][\w|\-\>]+', patronRules.group(), re.I)
            if objRul:
                self.grammarEdit.setText(self.grammarEdit.toPlainText()+objRul.group()+"\n")











