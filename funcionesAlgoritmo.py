#http://edupython.blogspot.com/2016/06/combinaciones-permutaciones-y-otras.html

def permuta(c):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c.
    """
    if len(c) == 0:
        return [[]]
    return sum([inserta_multiple(c[0], s)
                for s in permuta(c[1:])],
               [])

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

