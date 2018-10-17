#^es el inicio de la linea y el $ es el final de la linea
# el "." es cualquier caracter de la linea
#/s cualquier espacio de la linea
#+ es uno a mas y +? una o mas
# | es un o, encuenta la primera alternativa
#{n} exactamemente n veces
# (.)\1+ --> encuentra 'aaaa' y 'cc'.
#(.+)\1+ --> también encuentra 'abab' y '123123'
#(['"]?)(\d+)\1 --> encuentra '"13" (entre comillas dobles), o '4' (entre comillas simples) o 77 (sin comillas) etc.
#Pruebas de Carolina-------------------------------------------------------------------------
#(?P<aaa>)nombrar grupos
#prueba I bought a B of As W my Bgage from T S.
#""" respetar lo de adentro
import re

syntaxre = r"""(?mx)
^(?: 
  (?: (?P<comment> \% .* ) ) |
  (?: (?P<blank>   \s*  ) (?: \n | $ )  ) |
  (?: (?P<rule> (?P<pat> .+? ) \s+ -> \s+ (?P<repl> .*?[^.] ) (?P<term> \.)? ) )
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
P2: xβ -> .
P3: x -> βx (P1)
"""

def correrAlgoritmo(self):
    #self.runButton.clicked.connect(self.printText.clear)
    self.saveRegistryButton.setEnabled(True)
    texto = self.lineEdit.text()
    grammar= self.grammarEdit.toPlainText()
    self.printText.clear()
    self.printText.append("#PRUEBA"+ "\n")
    self.printText.append("LINEA DE ENTRADA: "+ texto + "\n")

    self.printText.append("\n"+"RESULTADO:  "+ remplazarReglas(self,texto,extraerreglas(grammar)))


def debug(self):
    texto = self.lineEdit.text()
    grammar = self.grammarEdit.toPlainText()
    self.printText.append(remplazarDebug(self, texto, extraerreglas(grammar)))

def extraerreglas(grammar):
    return [(matchobj.group('pat'), matchobj.group('repl'), bool(matchobj.group('term')))
            for matchobj in re.finditer(syntaxre, grammar)#Encuentre todas las subcadenas donde coincida la RE, y las devuelve como un iterador.
            if matchobj.group('rule')]#va metiedo a la lista si cumple lo de la reglas Ejm:[('"A"',apple,False)] Devuelve la cadena emparejada por el RE
def remplazarReglas(self,text, grammar):
    while True:
        for pat, repl, term in grammar:
            if pat == "Λ":
                t = list(text)
                self.printText.append(text + "  ->  ")
                text = text.replace(t[0], repl, 1)
                self.printText.insertPlainText(text)
            else:
                if pat in text:
                    if repl == "Λ":
                        self.printText.append(text + "  ->  ")
                        text = text.replace(pat,"", 1)
                        self.printText.insertPlainText(text)
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




#Pruebas de Carolina-------------------------------------------------------------------------

