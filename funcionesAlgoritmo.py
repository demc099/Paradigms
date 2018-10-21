#^es el inicio de la linea y el $ es el final de la linea
# el "." es cualquier caracter de la linea
# | es un o, encuenta la primera alternativa
#/s cualquier espacio de la linea
#+ es uno a mas y +? una o mas
#{n} exactamemente n veces
# (.)\1+ --> encuentra 'aaaa' y 'cc'.
#(.+)\1+ --> también encuentra 'abab' y '123123'
#(['"]?)(\d+)\1 --> encuentra '"13" (entre comillas dobles), o '4' (entre comillas simples) o 77 (sin comillas) etc.
#Pruebas de Carolina-------------------------------------------------------------------------
#(?P<aaa>)nombrar grupos
#prueba I bought a B of As W my Bgage from T S.
#""" respetar lo de adentro
#(?: (?P < rule > (?P < e1 >  \w+?:)? (?P < pat >.+?) \s + -> \s + (?P < repl >.* ?[^.])(?P < term > \.)? ([(](?P < e2 >  \w+?)[)])?))
# def extraerreglas(grammar):
#     return [(matchobj.group('e1'),matchobj.group('pat'), matchobj.group('repl'), bool(matchobj.group('term')),matchobj.group('e2'))
#             for matchobj in re.finditer(syntaxre, grammar)#Encuentre todas las subcadenas donde coincida la RE, y las devuelve como un iterador.
#             if matchobj.group('rule')]#va metiedo a la lista si cumple lo de la reglas Ejm:[('"A"',apple,False)] Devuelve la cadena emparejada por el RE

import re
from PyQt5.QtWidgets import *

syntaxre = r"""(?mx)
^(?: 
  (?: (?P<comment> \% .* ) ) |
  (?: (?P<blank>   \s*  ) (?: \n | $ )  ) |
  (?: (?P<rule> (?P<pat> .+? ) \s+ -> \s+ (?P<repl> .*?[^.] ) (?P<term> \.)? ))
)$
"""

syntaxre1 = r"""(?mx)
^(?: 
  (?: (?P<comment> \% .* ) ) |
  (?: (?P<blank>   \s*  ) (?: \n | $ )  ) |
  (?: (?P<rule> (?P<e1>\w+?:)? (?P<pat> .+? ) \s+ -> \s+ (?P<repl> .*?[^.] ) (?P<term> \.)? ([(](?P<e2>\w+?)[)])?   ))
)$
"""

def debug(self, texto):
    self.clearRegistryButton.setEnabled(True)
    self.saveRegistryButton.setEnabled(True)
    #texto = self.lineEdit.text()
    grammar= self.grammarEdit.toPlainText()
    variables = self.varsEdit.text()
    #self.printText.clear()

    #self.printText.append(remplazardebug(self,texto,extraerreglas(grammar), variables) + "\n")
    self.debugButton.setEnabled(False)
    self.printText.append(remplazardebug(self, texto, extraerreglas(grammar), variables))

    grammar= self.grammarEdit.toPlainText().replace('"', '')
    grammar= grammar.replace('->', ' -> ')


def correrAlgoritmo(self):
    self.clearRegistryButton.setEnabled(True)
    self.saveRegistryButton.setEnabled(True)
    texto = self.lineEdit.text()
    #grammar= self.grammarEdit.toPlainText()
    grammar = self.grammarEdit.toPlainText().replace('"', '')
    self.printText.clear()
    self.printText.append("#PRUEBA"+ "\n")
    self.printText.append("LINEA DE ENTRADA: "+ texto + "\n")
    self.printText.append("\n"+"RESULTADO:  "+ reemplazarReglas(self,texto,extraerreglas(grammar)))

def extraerreglas(grammar):
    return [(matchobj.group('pat'), matchobj.group('repl'), bool(matchobj.group('term')))
            for matchobj in re.finditer(syntaxre, grammar)#Encuentre todas las subcadenas donde coincida la RE, y las devuelve como un iterador.
            if matchobj.group('rule')]#va metiedo a la lista si cumple lo de la reglas Ejm:[('"A"',apple,False)] Devuelve la cadena emparejada por el RE

def reemplazarReglas(self, text, grammar):
    while True:
        for pat, repl, term in grammar:
            te = hayVars(self,text,pat,repl)
            if te:
                self.printText.append(text + "  ->  ")
                text = te
                self.printText.insertPlainText(text)
                if term:
                    return text
                break
            else:
                if pat == "Λ":
                    t = list(text)
                    self.printText.append(text + "  ->  ")
                    text = text.replace(t[0], repl+t[0], 1)
                    self.printText.insertPlainText(text)
                    if term:
                        return text
                    break
                else:
                    if pat in text:
                        if repl == "Λ":
                            self.printText.append(text + "  ->  ")
                            text = text.replace(pat, "", 1)
                            self.printText.insertPlainText(text)
                            if term:
                                return text
                            break
                        else:
                            self.printText.append(text+"  ->  ")
                            text = text.replace(pat, repl, 1)
                            self.printText.insertPlainText(text)
                            if term:
                              return text
                            break
        else:
            return text# y si recorre el for y el pat no esta en la gramatica

def hayVars(self, text,pat,repl):
    listaVar = list(self.varsEdit.text())
    listapat = list(pat)
    comp = [item for item in listaVar if item in listapat]
    if len(comp) > 0:
        te = pruebaEx(self,pat,repl,text)
        return te

def pruebaEx(self,pat,repl,text):
    rep2=list(repl)
    listaVar = list(self.varsEdit.text())
    listaMar = list(self.markersEdit.text())
    listapat = list(pat)
    listrem = []
    comp = [listapat.index(item) for item in listapat if item in listaVar]
    if len(comp) > 0:
        text1 = text
        cont=0
        lista = []
        bool=False
        while len(comp)<len(text1) and cont<len(text1):
            i=0
            d=0
            while i < len(comp):
                if d in comp:
                    if text1[comp[i]] in listaMar:
                        bool = True
                        break
                    else:
                     p1 = pat[comp[i]], text1[comp[i]]
                     lista.append(p1[1])
                     rep2= [w.replace(p1[0],p1[1]) for w in rep2]
                     listrem.append(p1)
                     i+=1
                     d+=1
                else:
                    lista.append(listapat[d])
                    d+=1
                    if i+1 == len(pat):
                        i+=1

            pats = ''.join(map(str, lista))
            f=len(pat)+1
            if bool==True:
                lista.clear()
                text1 = text1[1:]
                cont += 1
                bool = False
            else:
                if pats in text[cont:cont+f]:
                    rep1 = ''.join(map(str, rep2))
                    if repl == "Λ":
                        text = text.replace(pats, "")
                    else:
                        text = text.replace(pats, rep1)
                    return text
                else:
                    text1 = text1[1:]
                    lista.clear()
                    bool=False
                    cont += 1

def remplazardebug(self, text, grammar,vars):
    while True:
        for pat, repl, term in grammar:
            if (self.deb == True and self.texto != " "):
                te = hayVars(self,text,pat,repl,vars)
                if te:
                    self.printText.append(text + "  ->  ")
                    text = te
                    self.printText.insertPlainText(text)
                    self.deb = False
                    self.texto = text
                    if term:
                        self.texto = " "
                        self.nextButton.setEnabled(False)
                        self.debugButton.setEnabled(True)
                        QMessageBox.information(self, "Informacion", "Fin del debug", QMessageBox.Ok)
                        return " "
                    break
                else:
                    if pat == "Λ":
                        t = list(text)
                        self.printText.append(text + "  ->  ")
                        text = text.replace(t[0], repl, 1)
                        self.printText.insertPlainText(text)
                        self.deb = False
                        self.texto = text
                        #print(self.texto + " dos")
                    else:
                        if pat in text:
                            if repl == "Λ":
                                res=espacioV(self, text, pat, repl)
                                text=res
                                self.deb = False
                                self.texto = text
                            else:
                                self.printText.append(text+"  ->  ")
                                text = text.replace(pat, repl, 1)
                                self.printText.insertPlainText(text)
                                self.deb = False
                                self.texto = text
                                #print(self.texto + " tres")
                                if term:
                                    self.texto = " "
                                    self.nextButton.setEnabled(False)
                                    self.debugButton.setEnabled(True)
                                    QMessageBox.information(self, "Informacion", "Fin del debug", QMessageBox.Ok)
                                    return " "
                                break
        else:
            #print(text)
            return " "# y si recorre el for y el pat no esta en la gramatica

def cambiarX(pat, repl, text, vars):
    cp = 0

    while cp < len(pat):
        p = pat[cp]
        if p in vars:
            c = 0
            while c < len(text):

                if pat.replace(p, text[c]) in text:
                    pat = pat.replace(p, text[c])
                    repl = repl.replace(p, text[c])
                    if repl == "Λ":
                        text = text.replace(pat, "")
                    else:
                        text = text.replace(pat, repl)
                    return text
                else:
                    c += 1

        cp += 1

def espacioV(self,text,pat,rep1):
    self.printText.append(text + "  ->  ")
    text = text.replace(pat, "", 1)
    self.printText.insertPlainText(text)

#Pruebas de Carolina-------------------------------------------------------------------------

def correrAlgoritmoPruebas(self):
    self.clearRegistryButton.setEnabled(True)
    self.saveRegistryButton.setEnabled(True)

    grammar= self.grammarEdit.toPlainText()
    variables = self.varsEdit.text()
    pruebas = str(self.fileEdit.toPlainText()).split('\n')

    self.printText.clear()

    for line in pruebas:
        if line != '\n' and line != '':
            self.printText.append("#PRUEBA"+ "\n")
            self.printText.append("LINEA DE ENTRADA: "+ line + "\n")

            self.printText.append("\n"+"RESULTADO:  "+ reemplazarReglas(self,line,extraerreglas(grammar), variables)+ "\n")



