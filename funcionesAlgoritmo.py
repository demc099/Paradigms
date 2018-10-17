#http://edupython.blogspot.com/2016/06/combinaciones-permutaciones-y-otras.html

# def permuta(c):
#     """Calcula y devuelve una lista con todas las
#        permutaciones posibles que se pueden hacer
#        con los elementos contenidos en c.
#     """
#     if len(c) == 0:
#         return [[]]
#     return sum([inserta_multiple(c[0], s)
#                 for s in permuta(c[1:])],
#                [])
import re

def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

def imprime_ordenado(c):
    
    """Imprime en la salida estándar todos los
       subconjuntos del conjunto c (una lista de
       listas) ordenados primero por tamaño y
       luego lexicográficamente. Cada subconjunto
       se imprime en su propia línea. Los
       elementos de los subconjuntos deben ser
       comparables entre sí, de otra forma puede
       ocurrir un TypeError.
    """
    for e in sorted(c, key=lambda s: (len(s), s)):
        print(e)
        

def algoritmo(self, linea, variables):
    c=linea+variables
    imprime_ordenado(potencia(c))
    
def leng(cadena):
    lenguaje= {'ab':'cd'}

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
syntaxre = r"""(?mx)
^(?: 
  (?: (?P<comment> \% .* ) ) |
  (?: (?P<blank>   \s*  ) (?: \n | $ )  ) |
  (?: (?P<rule>    (?P<pat> .+? ) \s+ -> \s+ (?P<term> \.)? (?P<repl> .+) ) )
)$
"""

grammar1 = """\
% This rules file is extracted from Wikipedia:
% http://en.wikipedia.org/wiki/Markov_Algorithm
A -> apple
B -> bag
S -> shop
T -> the
W -> PRUE
the shop -> my brother
a never used -> .terminating rule
"""
#abcd
grammar2 = """\
P1: βx -> xβ (P1)
P2: xβ -> .
P3: x -> βx (P1)
"""

def correrAlgoritmo(self):
    #self.runButton.clicked.connect(self.printText.clear)
    self.clearRegistryButton.setEnabled(True)
    self.saveRegistryButton.setEnabled(True)
    texto = self.lineEdit.text()
    grammar= self.grammarEdit.toPlainText()
    self.printText.clear()
    self.printText.append("#PRUEBA"+ "\n")
    self.printText.append("LINEA DE ENTRADA: "+ texto + "\n")

    self.printText.append("\n"+"RESULTADO:  "+ remplazarReglas(self,texto,extraerreglas(grammar1)))


def debug(self):
    texto = self.lineEdit.text()
    grammar = self.grammarEdit.toPlainText()
    self.printText.append(remplazarDebug(self, texto, extraerreglas(grammar)))

def extraerreglas(grammar):
    return [(matchobj.group('pat'), matchobj.group('repl'), bool(matchobj.group('term')))
            for matchobj in re.finditer(syntaxre, grammar1)#Encuentre todas las subcadenas donde coincida la RE, y las devuelve como un iterador.
            if matchobj.group('rule')]#va metiedo a la lista si cumple lo de la reglas Ejm:[('"A"',apple,False)] Devuelve la cadena emparejada por el RE
def remplazarReglas(self,text, grammar):
    while True:
        for pat, repl, term in grammar:
            if pat in text:
                self.printText.append(text+"  ->  ")
                text = text.replace(pat, repl, 1)
                self.printText.insertPlainText(text)
                if term:
                    return text
                break
        else:
            return text


def remplazarDebug(self, text, grammar):
    for pat, rep1, term in grammar:
        if pat in text:
            self.printText.append(text+"  ->  ")




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
