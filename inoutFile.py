from PyQt5.QtWidgets import QInputDialog

def guardarTxt(self):
     text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Digite el nombre del archivo donde desea guardar:')
     if ok:
            file = "./algoritmos/"+(str(text))+".txt"
            fo = open(file, "w")
     fo.write("#symbols "+self.symbolsEdit.text()+"\n")
     fo.write("#vars "+self.varsEdit.text()+"\n")
     fo.write("#markers "+self.markersEdit.text()+"\n")
     fo.close()

        
