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

import validaciones

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

def correrAlgoritmo(self):
    self.clearRegistryButton.setEnabled(True)
    self.saveRegistryButton.setEnabled(True)
    texto = self.lineEdit.text()
    if texto == "":
        validaciones.enviarMensError(self, "Ingrese una hilera de prueba")
    else:
        grammar = self.grammarEdit.toPlainText().replace('"', '')
        self.printText.clear()
        self.printText.append("#PRUEBA"+ "\n")
        self.printText.append("LINEA DE ENTRADA: "+ texto + "\n")
        self.printText.append("RESULTADO:  "+ reemplazarReglas(self,texto,extraerreglas(grammar)))

def extraerreglas(grammar):
    return [(matchobj.group('pat'), matchobj.group('repl'), bool(matchobj.group('term')))
            for matchobj in re.finditer(syntaxre, grammar)#Encuentre todas las subcadenas donde coincida la RE, y las devuelve como un iterador.
            if matchobj.group('rule')]#va metiedo a la lista si cumple lo de la reglas Ejm:[('"A"',apple,False)] Devuelve la cadena emparejada por el RE

def reemplazarReglas(self, text, grammar):
    while True:
        for pat, repl, term in grammar:
            te = hayVars(self,text,pat,repl)
            if te:
                if te[1] == True:
                    text = text.replace(te[0], "", 1)
                else:
                    #self.printText.append(text + "  ->  ")
                    text = te
                    #self.printText.insertPlainText(text)
                if term:
                    return text
                break
            else:
                if pat == "Λ":
                    t = list(text)
                    #self.printText.append(text + "  ->  ")
                    text = text.replace(t[0], repl+t[0], 1)
                    #self.printText.insertPlainText(text)
                    if term:
                        return text
                    break
                else:
                    if pat in text:
                        if repl == "Λ":
                            #self.printText.append(text + "  ->  ")
                            text = text.replace(pat, "", 1)
                            #self.printText.insertPlainText(text)
                            if term:
                                return text
                            break
                        else:
                            #self.printText.append(text+"  ->  ")
                            text = text.replace(pat, repl, 1)
                            #self.printText.insertPlainText(text)
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
        te = pruebaEx(self,pat,repl,text,listapat,listaVar)
        return te

def pruebaEx(self,pat,repl,text,listapat,listaVar):
    rep2=list(repl) #crea una lista del remplazo
    listaMar = list(self.markersEdit.text()) #lista de marcadores
    comp = [listapat.index(item) for item in listapat if item in listaVar] #comp es una lista que tiene la posicion de las variables en el pat
    if len(comp) > 0: # si el tamaño de com es mayor a 0 puede seguir, si no significa que no existen variables que comparar e intercambiar
        text1 = text #aqui igualo text1 a text xq ya que con forme pase el metodo a text1 se le va a ir eliminando el primer caracter
        cont=0 #contador de recorrer el text
        lista = [] #lista vacia para ingresar el orden del nuevo pat
        bool=False # variable booleana que sirve para ver si el comp que entra es un marcador
        while len(pat)<=len(text1): #si el tamaño de comp y el contador sea menor al tamaño del texto1, en caso de que fuera mayor no entraria ya no habia suficiente text para ser remplazado
            a = len(pat)
            b = len(comp)
            c = len(text1)
            i=0 #contador del recorrido del comp
            d=0 #contador para ver si existe ese espacio en el comp
            while i < len(pat): # si i es menor a comp entonces entre
                if d in comp: # si d esta en el comp como una pos
                    if text1[comp[i]] in listaMar: #si el valor de text en la pos i es un marcador
                        bool = True
                        break
                    else:
                     p1 = pat[comp[i]], text1[comp[i]] # es la tupla de del  (pat en la pos i, text en la pos i)
                     lista.append(p1[1]) #agrego el text a la lista
                     rep2= [w.replace(p1[0],p1[1]) for w in rep2] # replazo toda var del pat que este en el stirng de remplazo
                     i+=1 #me devuelvo a recorrer el comp
                     d+=1 #subo una pos
                else: #si no esta el d en el comp, significa que aqui hay marcadores o variables, entonces se agregan de la siguiente forma para respetar el orden del pat
                    if d < len(pat):
                        lista.append(listapat[d]) #agrego a la lista el marcador
                        d+=1 #subo una pos
                        if i+1 == len(pat): # si es igual aumento uno para que no vuelva a recorrer el pat
                            i+=1
                    else:
                        i+=1

            if bool==True: #si se cumple se sale xq significa que no cumple la condicion pat
                lista.clear() #limpio la lista
                rep2 = list(repl)
                text1 = text1[1:] #elimino el primer valor del text1
                cont += 1 #recorro de nuevo el texto
                bool = False # convierto otra vez el bool

            else: # si no probar si existe la sustitucion
                pats = ''.join(map(str, lista))  # convierto la lista un string
                f = len(pat) + 1  # f es el tamaño del pat, se usa para obtener el texto de comparación

                if pats in text[cont:cont+f]: #existe el pat en el text
                    rep1 = ''.join(map(str, rep2)) # convierto la lista replazo un strirng
                    if repl == "Λ":
                        t2= [pats, True]#pat = pats#text = text.replace(pats, "", 1)#si remplazo fuera lambda en el texto dode este el pat lo remplazo por nada
                        return t2
                    else:
                        text = text.replace(pats, rep1) # remplzo el pat por el patron de sustitucion
                        return text #retorno el texto completo ya con la sustitucion aplicada

                else: # si no existe el pat en el texto
                    text1 = text1[1:]  # elimino el primer valor a texto1
                    lista.clear() #limpio la lista del pat
                    bool=False
                    rep2 = list(repl)
                    cont += 1 # recorro el text de nuevo



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


def debug(self, texto):
    self.clearRegistryButton.setEnabled(True)
    self.saveRegistryButton.setEnabled(True)
    grammar= self.grammarEdit.toPlainText()
    variables = self.varsEdit.text()
    grammar = self.grammarEdit.toPlainText().replace('"', '')
    #self.debugButton.setEnabled(False)
    self.printText.append(remplazardebug(self, texto, extraerreglas(grammar), variables))



def remplazardebug(self, text, grammar,vars):
    print("entro "+ self.texto)
    while True:
        for pat, repl, term in grammar:
            if (self.deb == True and self.texto != " "):
                te = hayVars(self,text,pat,repl)
                if te:
                    self.printText.append("Paso " + str(self.cont) + ": " + text + "  ->  ")
                    text = te
                    self.printText.insertPlainText(text)
                    self.deb = False
                    self.texto = text
                    print("fue el 1")
                    if term:
                        self.texto = " "
                        self.nextButton.setEnabled(False)
                        #QMessageBox.information(self, "Informacion", "Fin del debug", QMessageBox.Ok)
                        return " "
                        print("fue el 2")
                    break
                else:
                    if pat == "Λ":
                        t = list(text)
                        self.printText.append("Paso " + str(self.cont) + ": " + text + "  ->  ")
                        text = text.replace(t[0], repl+t[0], 1)
                        self.printText.insertPlainText(text)
                        self.deb = False
                        self.texto = text
                        print("fue el 3")
                        if term:
                            self.texto = " "
                            self.nextButton.setEnabled(False)
                            #QMessageBox.information(self, "Informacion", "Fin del debug", QMessageBox.Ok)
                            return " "
                            print("fue el 4")
                        break
                    else:
                        if pat in text:
                            if repl == "Λ":
                                self.printText.append("Paso " + str(self.cont) + ": " + text + "  ->  ")
                                text = text.replace(pat, "", 1)
                                self.printText.insertPlainText(text)
                                self.deb = False
                                self.texto = text
                                print("fue el 5")
                                if term:
                                    self.texto = " "
                                    self.nextButton.setEnabled(False)
                                    #QMessageBox.information(self, "Informacion", "Fin del debug", QMessageBox.Ok)
                                    return " "
                                    print("fue el 6")
                                break
                            else:
                                self.printText.append("Paso "+ str(self.cont) + ": " +text+"  ->  ")
                                print(self.cont)
                                text = text.replace(pat, repl, 1)
                                self.printText.insertPlainText(text)
                                self.deb = False
                                self.texto = text
                                if term:
                                    self.texto = " "
                                    self.nextButton.setEnabled(False)
                                    #QMessageBox.information(self, "Informacion", "Fin del debug", QMessageBox.Ok)
                                    return " "
                                    print("fue el 8")
                                break
        else:
            #print(text)
            return " "# y si recorre el for y el pat no esta en la gramatica



# Aplica el algoritmo linea por linea a un archivo que contiene hileras de prueba -------------------------------------------------------------------------

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



