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


grammar1 = """\
% This rules file is extracted from Wikipedia:
% http://en.wikipedia.org/wiki/Markov_Algorithm
A -> apple
B -> bag
S -> Λ.
T -> the
W -> PRUE
the shop -> my brother
"""
#abcd
grammar2 = """\
P1: βx -> xβ (P1)
P2: xβ -> Λ.
P3: x -> βx (P1)
"""

grammar2 = """\
βx -> xβ
xβ -> Λ.
x -> βx
"""

def correrAlgoritmo(self):
    self.clearRegistryButton.setEnabled(True)
    self.saveRegistryButton.setEnabled(True)
    texto = self.lineEdit.text()
    grammar= self.grammarEdit.toPlainText()
    variables = self.varsEdit.text()
    self.printText.clear()
    self.printText.append("#PRUEBA"+ "\n")
    self.printText.append("LINEA DE ENTRADA: "+ texto + "\n")

    self.printText.append("\n"+"RESULTADO:  "+ remplazarReglas(self,texto,extraerreglas(grammar), variables))


def debug(self):
    texto = self.lineEdit.text()
    grammar = self.grammarEdit.toPlainText()
    self.printText.append(remplazarDebug(self, texto, extraerreglas(grammar)))

def extraerreglas(grammar):
    return [(matchobj.group('pat'), matchobj.group('repl'), bool(matchobj.group('term')))
            for matchobj in re.finditer(syntaxre, grammar)#Encuentre todas las subcadenas donde coincida la RE, y las devuelve como un iterador.
            if matchobj.group('rule')]#va metiedo a la lista si cumple lo de la reglas Ejm:[('"A"',apple,False)] Devuelve la cadena emparejada por el RE

def remplazarReglas(self,text, grammar, vars):
    while True:
        for pat, repl, term in grammar:
            te = hayVars(self,text,pat,repl,vars)
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
                    text = text.replace(t[0], repl, 1)
                    self.printText.insertPlainText(text)
                else:
                    if pat in text:
                        if repl == "Λ":
                            res=espacioV(self, text, pat, repl)
                            text=res
                        else:
                            self.printText.append(text+"  ->  ")
                            text = text.replace(pat, repl, 1)
                            self.printText.insertPlainText(text)
                            if term:
                                return text
                            break
        else:
            return text# y si recorre el for y el pat no esta en la gramatica


def remplazarDebug(self, text, grammar):
    for pat, rep1, term in grammar:
        if pat in text:
            self.printText.append(text+"  ->  ")


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
    #self.runButton.clicked.connect(self.printText.clear)
    self.clearRegistryButton.setEnabled(True)
    self.saveRegistryButton.setEnabled(True)
    grammar= self.grammarEdit.toPlainText()
    pruebas = str(self.fileEdit.toPlainText()).split('\n')
    self.printText.clear()

    for line in pruebas:
       self.printText.append("#PRUEBA"+ "\n")
       self.printText.append("LINEA DE ENTRADA: "+ line + "\n")
       self.printText.append("\n"+"RESULTADO:  "+ remplazarReglas(self,line,extraerreglas(grammar)) + "\n")

def hayVars(self, text,pat,repl,vars):
    listaVar = list(self.varsEdit.text())
    listatext = list(pat)
    comp = [item for item in listaVar if item in listatext]
    if len(comp) > 0:
        te = cambiarX(pat, repl, text, vars)
        return te

