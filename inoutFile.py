from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import re

"""Este es el método encargado de abrir el archivo txt o xml donde se desea guardar y pasarle la ruta de este al método validarFormatoGuardar"""
def guardar(self):
    fileName, _ = QFileDialog.getSaveFileName(self, "Guardar", "","Text Files (*.txt);;Xml Files (*.xml)")
    if fileName:
        validarFormatoGuardar(self, fileName)


"""Este método recibe la ruta del archivo donde se desea guardar y verifica por medio de expresiones regulares si se trata de un archivo .txt o de un archivo .xml 
para luego pasar esta ruta al método que según corresponda; ya que el proceso de guardar un .txt se realiza diferente al de guardar un .xml"""
def validarFormatoGuardar(self, fileName):
    patronTxt = re.match('^(\w):\/[(\w+\s?\w+)(áéíóúñ\_\#\-)+\/?]+\.txt$', fileName, re.I)
    patronXml = re.match('^(\w):\/[(\w+\s?\w+)(áéíóúñ\_\#\-)+\/?]+\.xml$', fileName, re.I)
    if (patronTxt):
        guardarTxt(self, fileName)
    if (patronXml):
        guardarXml(self, fileName)


"""Este método recibe la ruta del archivo donde se desea guardar, lo abre y guarda los simbolos (que los toma del TextLine para ingresar simbolos), variables (que los toma del 
TextLine para ingresar variables), marcadores (que los toma del TextLine para ingresar marcadores), reglas (que los toma del TextLine para ingresar reglas) y comentarios (si existen
los toma del TextEdit para ingresar reglas) en el archivo. Se guardan los simbolos con la palabra #symbols, las variables con la palabra #vars y los marcadores con la palabra 
#markers. En el caso de las reglas y los comentarios se guarda de uno por uno, respetando los saltos de línea"""
def guardarTxt(self, fileName):
    file = open(fileName, "w", encoding='utf-8-sig')
    file.write("#symbols "+self.symbolsEdit.text()+"\n")
    file.write("#vars "+self.varsEdit.text()+"\n")
    file.write("#markers "+self.markersEdit.text()+"\n")
    lines = str(self.grammarEdit.toPlainText()).split('\n')
    for line in lines:
        if (re.match("%[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}\s]+", line, re.I) or re.match("[\"?\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}\s\"?]+\-\>[\"?\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}\s\"?]", line, re.I)):
            #[\w\(\)\[\]\ * \+\¿\?\!\  # \¡\$\&\%\{\}]
            file.write(line+ "\n")
    file.close()


"""Este método recibe la ruta del archivo donde se desea guardar, lo abre y guarda los simbolos, variables, marcadores, reglas y comentarios (si existen) en el archivo. 
Se guardan los simbolos entre las etiquetas <symbols> </symbols>, las variables entre las etiquetas <vars></vars>, los marcadores entre las etiquetas <markers></markers>, las reglas entre las
 etiquetas <rules></rules> y los comentarios entre las etiquetas <comment></comment>."""
def guardarXml(self, fileName):
    file = open(fileName, "w", encoding='utf-8-sig')
    file.write("<?xml version='1.0' encoding='UTF-8'?>"+"\n")
    file.write("<algoritmo>"+"\n")
    file.write("<symbols>"+self.symbolsEdit.text()+"</symbols>"+"\n")
    file.write("<vars>"+self.varsEdit.text()+"</vars>"+"\n")
    file.write("<markers>"+self.markersEdit.text() + "</markers>"+"\n")
    lines = str(self.grammarEdit.toPlainText()).split('\n')
    for line in lines:
        if re.match("%[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}\s]+", line, re.I):
            file.write("<comment>"+line+"</comment>"+"\n")
        if re.match("[\"?\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}\s\"?]+\-\>[\"?\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}\s\"?]", line, re.I):
            file.write("<rules>"+line+"</rules>"+"\n")
    file.write('</algoritmo>')


"""Este es el método encargado de abrir el archivo txt o xml de donde se desea cargar y pasarle la ruta de este al método validarFormatoCargar"""
def cargar(self):
    fileName, _ = QFileDialog.getOpenFileName(self, "Abrir como", "","Text Files (*.txt);;Xml Files (*.xml)")
    if fileName:
        validarFormatoCargar(self, fileName)


"""Este método recibe la ruta del archivo a cargar y verifica por medio de expresiones regulares si se trata de un archivo .txt o de un archivo .xml 
para luego pasar esta ruta al método que según corresponda; ya que el proceso de cargar un .txt se realiza diferente al de cargar un .xml"""
def validarFormatoCargar(self, fileName):
    patronTxt = re.match('^(\w):\/[(\w+\s?\w+)(áéíóúñ\_\#\-)+\/?]+\.txt$', fileName, re.I)
    patronXml = re.match('^(\w):\/[(\w+\s?\w+)(áéíóúñ\_\#\-)+\/?]+\.xml$', fileName, re.I)
    if(patronTxt):
        cargarTxt(self, fileName)
    if(patronXml):
        cargarXml(self, fileName)


"""Este metodo se encarga de extraer cada línea del archivo .txt de donde se desea cargar la información, y se verifica por medio de expresiones regulares cual línea
pertence al alfabeto (simbolos), variables, marcadores, reglas y comentarios."""
def cargarTxt(self, fileName):
    file = open(fileName, 'r', encoding='utf-8-sig')
    lines = file.readlines()
    self.grammarEdit.setText("")
    for line in lines:
        #line = line.replace("\ufeff#symbols", "\#symbols")
        patronSym = re.search('^\#symbols\s[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}\s]+', line, re.UNICODE)
        patronVars = re.search('^\#vars\s[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}]+', line, re.UNICODE)
        patronMark = re.search('^\#markers\s[a-zA-Z0-9áéíóúàèìòùäëïöüαβγδεζηθικλμνξοπρσςτυφχψωΛ]+', line, re.UNICODE)
        patronRules = re.search('^(\"[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}\s]+\"|[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}]+)\s?\-\>\s?(\"[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}\s]+\"|[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}\s]+)\.?', line,re.UNICODE)
        patronComment = re.search('^%[\w\s]+', line, re.UNICODE)
        if patronSym:
            pr = line.replace("#symbols ","")
            self.symbolsEdit.setText(pr.rstrip())
            self.symbolsEdit.setStyleSheet("color: blue; border: 1px solid green;")
        if patronVars:
            pr = line.replace("#vars ","")
            self.varsEdit.setText(pr.rstrip())
            self.varsEdit.setStyleSheet("color: blue; border: 1px solid green;")
        if patronMark:
            pr = line.replace("#markers ","")
            self.markersEdit.setText(pr.rstrip())
            self.markersEdit.setStyleSheet("color: blue; border: 1px solid green;")
        if patronRules:
            self.grammarEdit.setText(self.grammarEdit.toPlainText()+line)
        if patronComment:
            self.grammarEdit.setText(self.grammarEdit.toPlainText()+line)
    file.close()
    

"""Este metodo se encarga de extraer cada línea del archivo .xml de donde se desea cargar la información, y se verifica por medio de expresiones regulares cual línea
pertenece al alfabeto (simbolos), variables, marcadores, reglas y comentarios."""
def cargarXml(self, fileName):
    file = open(fileName, 'r', encoding='utf-8-sig')
    lines = file.readlines()
    self.grammarEdit.setText("")
    for line in lines:
        patronSym = re.search('^\<symbols\>[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}]+\<\/symbols\>', line, re.UNICODE)
        patronVars = re.search('^\<vars\>[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}]+\<\/vars\>', line, re.UNICODE)
        patronMark = re.search('^\<markers\>[a-zA-Z0-9áéíóúàèìòùäëïöüαβγδεζηθικλμνξοπρσςτυφχψωΛ]+\<\/markers\>', line, re.UNICODE)
        patronRules = re.search('^\<rules\>(\"[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}\s]+\"|[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}]+)\s?\-\>\s?(\"[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}\s]+\"|[\w\(\)\[\]\*\+\¿\?\!\#\¡\$\&\%\{\}]+)\.?\<\/rules\>', line,re.UNICODE)
        patronComment = re.search('^\<comment\>%[\w\s]+\<\/comment\>', line, re.UNICODE)
        if patronSym:
            pr1 = line.replace("<symbols>","")
            pr = pr1.replace("</symbols>","")
            self.symbolsEdit.setText(pr.rstrip())
            self.symbolsEdit.setStyleSheet("color: blue; border: 1px solid green;")
        if patronVars:
            pr2 = line.replace("<vars>","")
            pr = pr2.replace("</vars>","")
            self.varsEdit.setText(pr.rstrip())
            self.varsEdit.setStyleSheet("color: blue; border: 1px solid green;")
        if patronMark:
            pr3 = line.replace("<markers>","")
            pr = pr3.replace("</markers>","")
            self.markersEdit.setText(pr.rstrip())
            self.markersEdit.setStyleSheet("color: blue; border: 1px solid green;")
        if patronRules:
            pr4 = line.replace("<rules>","")
            self.grammarEdit.setText(self.grammarEdit.toPlainText()+pr4.replace("</rules>",""))
        if patronComment:
            pr5 = line.replace("<comment>","")
            self.grammarEdit.setText(self.grammarEdit.toPlainText() + pr5.replace("</comment>", ""))
    file.close()

#-------------------- Guardar resultado que genera el algoritmo --------------------

"""Este metodo permite guardar los resultados de la o las hileras luego de aplicar el algoritmo sobre ellas """
def guardarResultado(self):
    fileName, _ = QFileDialog.getSaveFileName(self, "Guardar", "", "Text Files (*.txt)")
    if fileName:
        file = open(fileName, "w", encoding='utf-8-sig')
        resultado = self.printText.toPlainText()
        if resultado != " ":
            file.write(resultado)
        else:
            QMessageBox.critical(self, "Error", "No hay resultados que guardar", QMessageBox.Ok)


#-------------------- Funciones Cargar y  Guardar Archivo de Pruebas --------------------

"""Este método permite guardar un archivo con hileras de prueba, esto debido a que si el usuario desea modificar las hileras para luego correrlas luego 
se pueden volver a guardar """
def guardarArchivoPrueba(self):
    fileNamePrueba, _ = QFileDialog.getSaveFileName(self, "Guardar", "","Text Files (*.txt)")
    if fileNamePrueba:
        fileNamePrueba = open(fileNamePrueba, "w", encoding='utf-8-sig')
        fileNamePrueba.write(self.fileEdit.toPlainText() + "\n")
    fileNamePrueba.close()

"""Este método permite cargar un archivo con hileras de prueba para luego poder aplicar sobre cada una de ellas un algoritmo"""
def cargarArchivoPrueba(self):
    fileNamePrueba, _ = QFileDialog.getOpenFileName(self, "Abrir Documento de Pruebas", "","Text Files (*.txt)")
    if fileNamePrueba:
        file = open(fileNamePrueba, 'r', encoding='utf-8-sig')
        lines = file.readlines()
        self.fileEdit.setText("")
        for line in lines:
            if line != " ":
                patronPrueba = re.search('^[\w]+', line, re.UNICODE)
                if patronPrueba and line != '\n':
                    self.fileEdit.setText(self.fileEdit.toPlainText() + line)

        #self.fileEdit.setText(self.fileEdit.toPlainText().rstrip('\n'))

        file.close()

