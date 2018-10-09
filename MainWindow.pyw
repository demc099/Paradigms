import sys

from PyQt5.QtGui import QIcon, QPixmap, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox
from PyQt5 import uic

class Ventana(QMainWindow):   
 def __init__(self):
  QMainWindow.__init__(self)
  uic.loadUi("MainWindowInterfaz.ui", self)
  self.setWindowTitle("Traductor")

  #Poner imagenes a los botones
  self.putButton.setIcon(QIcon('image/plus.png'))
  self.removeButton.setIcon( QIcon('image/remove.png'))
  self.cancelButton.setIcon(QIcon('image/cancelar.png'))
  self.saveButton.setIcon(QIcon('image/guardar.png'))
  self.runButton.setIcon(QIcon('image/run.png'))
  self.nextButton.setIcon(QIcon('image/siguiente.png'))

  #Creacion del menu de la ventana
  menu= self.menuBar()
  menuArchivo = menu.addMenu("Archivo")
  menuHerramientas = menu.addMenu("Herramientas")
  menuPrueba = menu.addMenu("Algoritmos de prueba")

  #Agregar elementos a los menus principales
  menuA_nuevo = QAction(QIcon(),"Nuevo",self)
  menuArchivo.addAction(menuA_nuevo)

  menuA_abrir = QAction(QIcon(), "Abrir", self)
  menuArchivo.addAction(menuA_abrir)

  menuA_guardar = QAction(QIcon(), "Guardar", self)
  menuArchivo.addAction(menuA_guardar)

  menuA_salir = QAction(QIcon(), "Salir", self)
  menuA_salir.triggered.connect(self.menuArchivoSalir)
  menuArchivo.addAction(menuA_salir)

  menuH_paleta = QAction(QIcon(), "Paleta de caracteres", self)
  menuH_paleta.setShortcut("Ctrl+p")
  menuH_paleta.setStatusTip("Abrir la paleta de caracteres")
  menuHerramientas.addAction(menuH_paleta)

  menuH_cargarArchivo = QAction(QIcon(), "Cargar archivo de prueba", self)
  menuHerramientas.addAction(menuH_cargarArchivo)


  menuP_1 = QAction(QIcon(), "Invertir una hilera", self)
  menuPrueba.addAction(menuP_1)
  menuP_2 = QAction(QIcon(), "Duplicar hilera", self)
  menuPrueba.addAction(menuP_2)
  menuP_3 = QAction(QIcon(), "Palindromo", self)
  menuPrueba.addAction(menuP_3)
  menuP_4 = QAction(QIcon(), "Binario a unario", self)
  menuPrueba.addAction(menuP_4)
  menuP_5 = QAction(QIcon(), "Suma binarios", self)
  menuPrueba.addAction(menuP_5)
  menuP_6 = QAction(QIcon(), "Triplicar binarios", self)
  menuPrueba.addAction(menuP_6)
  menuP_7 = QAction(QIcon(), "Multiplicación binarios", self)
  menuPrueba.addAction(menuP_7)
  menuP_8 = QAction(QIcon(), "Suma decimales", self)
  menuPrueba.addAction(menuP_8)
  menuP_9 = QAction(QIcon(), "Eliminar caracteres repetidos consecutivos", self)
  menuPrueba.addAction(menuP_9)
  menuP_10 = QAction(QIcon(), "Paréntesis balanceados", self)
  menuPrueba.addAction(menuP_10)

  # Creacion de la tabla
  self.tableWidget.setColumnCount(2)
  self.tableWidget.setRowCount(1)
  self.tableWidget.setColumnWidth(0, 140)
  self.tableWidget.setColumnWidth(1, 155)
  self.tableWidget.setHorizontalHeaderLabels(("Reglas de producción","Reglas de sustitución"))

  #quitar y poner filas
  self.putButton.clicked.connect(self.agregarFila)
  self.removeButton.clicked.connect(self.quitarFila)

 def menuArchivoSalir(self):
   QMessageBox.question(self, "Mensaje", "Seguro quiere salir", QMessageBox.Yes, QMessageBox.No)

 def agregarFila(self):
  self.tableWidget.insertRow(self.tableWidget.rowCount())

 def quitarFila(self):
  indices = self.tableWidget.selectionModel().selectedRows()
  for index in sorted(indices):
   self.tableWidget.removeRow(index.row())

 def prueba(self):
  self.printText.setText("Prueba #1"+ self.symbolsEdit.text())

app = QApplication(sys.argv)
_ventana = Ventana()
_ventana.show()
app.exec_()
