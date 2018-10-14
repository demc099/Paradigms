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

#Pruebas de Carolina-------------------------------------------------------------------------
#prueba I bought a B of As W my Bgage from T S.
def correrAlgoritmo(self):
    stepNum=1
    texto = self.lineEdit.text()
    self.printText.append("STEP")
    stepNum+=1
    self.printText.append(texto)
    self.printText.append(remplazarReglas(texto,extraerreglas(grammar1)))

    # "x": ['']
    # texto1 = []
    # i=0
    # while i < len(texto):
    #     texto1.append("x")
    #     i+=1
    # else:
    #     print(texto1)
    #
    # a="abcdefghijklmnopqrstuvwxyz0123456789"
    # v="xyz"
    # m="αβγδ"
    # rBusqueda=["βx","xβ","x"]
    # rSustitucion=["xβ","Λ.","βx"]
    # listav= list(v)
    # print(listav)
    # listav[0]
    # i = 0
    # #while i < len(rBusqueda):

syntaxre = r"""(?mx)
^(?: 
  (?: (?P<comment> \% .* ) ) |
  (?: (?P<blank>   \s*  ) (?: \n | $ )  ) |
  (?: (?P<rule>    (?P<pat>.+?) \s+ ->\s+(?P<term> \.)? (?P<repl> .+) ) )
)$
"""

grammar1 = """\
% This rules file is extracted from Wikipedia:
% http://en.wikipedia.org/wiki/Markov_Algorithm

A -> apple
B -> bag
S -> shop
T -> the
W-> HOla
the shop -> my brother
a never used -> .terminating rule

"""

def extraerreglas(grammar):
    return [(matchobj.group('pat'), matchobj.group('repl'), bool(matchobj.group('term')))
            for matchobj in re.finditer(syntaxre, grammar)
            if matchobj.group('rule')]

def remplazarReglas(text, grammar):
    while True:
        for pat, repl, term in grammar:
            if pat in text:
                text = text.replace(pat, repl, 1)
                if term:
                    return text
                break
        else:
            return text


#Pruebas de Carolina-------------------------------------------------------------------------

