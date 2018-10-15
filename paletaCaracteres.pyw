import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
class Caracteres(QDialog):
 
    def __init__(self, parent=None):
        super(Caracteres, self).__init__()
        self.parent = parent

        self.title = 'Caracteres Especiales.'
        self.left = 400
        self.top = 90
        self.width = 220
        self.height = 100
        
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setMaximumSize(self.width, self.height)
        self.setWindowIcon(QIcon('image/caracter.png'))

        self.createGridLayout()

        #self.show()


    #----- Funcion para Crear los QGroupBox con los botones correspondientes -----
    def createGridLayout(self):    
        titleMarker = u'&Alfabeto Griego'
        title = u'& Simbolos'

        alignment = Qt.AlignHCenter
        
        horizontalGroupBoxMarker = QGroupBox(titleMarker)
        horizontalGroupBoxMarker.setAlignment(alignment)
      
        horizontalGroupBox = QGroupBox(title)
        horizontalGroupBox.setAlignment(alignment)

        layoutMarker = QGridLayout()
        layoutMarker.setColumnStretch(1, 4)
        layoutMarker.setColumnStretch(2, 4)

        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
 
        #----- Botones Para los Caracteres Especiales de los Marcadores -----
        button = QPushButton('α', self)
        button.setStyleSheet("font-size: 14px; color: black;")
        button.clicked.connect(lambda:self.on_click(button))

        button1 = QPushButton('β', self)
        button1.setStyleSheet("font-size: 14px; color: black;")
        button1.clicked.connect(lambda:self.on_click(button1))

        button2 = QPushButton('γ', self)
        button2.setStyleSheet("font-size: 14px; color: black;")
        button2.clicked.connect(lambda:self.on_click(button2))
        
        button3 = QPushButton('δ', self)
        button3.setStyleSheet("font-size: 14px; color: black;")
        button3.clicked.connect(lambda:self.on_click(button3))
        
        button4 = QPushButton('ε', self)
        button4.setStyleSheet("font-size: 14px; color: black;")
        button4.clicked.connect(lambda:self.on_click(button4))
        
        button5 = QPushButton('ζ', self)
        button5.setStyleSheet("font-size: 14px; color: black;")
        button5.clicked.connect(lambda:self.on_click(button5))
        
        button6 = QPushButton('η', self)
        button6.setStyleSheet("font-size: 14px; color: black;")
        button6.clicked.connect(lambda:self.on_click(button6))
        
        button7 = QPushButton('θ', self)
        button7.setStyleSheet("font-size: 14px; color: black;")
        button7.clicked.connect(lambda:self.on_click(button7))
        
        button8 = QPushButton('ι', self)
        button8.setStyleSheet("font-size: 14px; color: black;")
        button8.clicked.connect(lambda:self.on_click(button8))
        
        button9 = QPushButton('κ', self)
        button9.setStyleSheet("font-size: 14px; color: black;")
        button9.clicked.connect(lambda:self.on_click(button9))
        
        button10 = QPushButton('λ', self)
        button10.setStyleSheet("font-size: 14px; color: black;")
        button10.clicked.connect(lambda:self.on_click(button10))
        
        button11 = QPushButton('μ', self)
        button11.setStyleSheet("font-size: 14px; color: black;")
        button11.clicked.connect(lambda:self.on_click(button11))
        
        button12 = QPushButton('ν', self)
        button12.setStyleSheet("font-size: 14px; color: black;")
        button12.clicked.connect(lambda:self.on_click(button12))
        
        button13 = QPushButton('ξ', self)
        button13.setStyleSheet("font-size: 14px; color: black;")
        button13.clicked.connect(lambda:self.on_click(button13))
        
        button14 = QPushButton('ο', self)
        button14.setStyleSheet("font-size: 14px; color: black;")
        button14.clicked.connect(lambda:self.on_click(button14))
        
        button15 = QPushButton('π', self)
        button15.setStyleSheet("font-size: 14px; color: black;")
        button15.clicked.connect(lambda:self.on_click(button15))
        
        button16 = QPushButton('ρ', self)
        button16.setStyleSheet("font-size: 14px; color: black;")
        button16.clicked.connect(lambda:self.on_click(button16))
        
        button17 = QPushButton('σ', self)
        button17.setStyleSheet("font-size: 14px; color: black;")
        button17.clicked.connect(lambda:self.on_click(button17))

        button18 = QPushButton('ς', self)
        button18.setStyleSheet("font-size: 14px; color: black;")
        button18.clicked.connect(lambda:self.on_click(button18))

        button19 = QPushButton('τ', self)
        button19.setStyleSheet("font-size: 14px; color: black;")
        button19.clicked.connect(lambda:self.on_click(button19))
        
        button20 = QPushButton('υ', self)
        button20.setStyleSheet("font-size: 14px; color: black;")
        button20.clicked.connect(lambda:self.on_click(button20))

        button21 = QPushButton('φ', self)
        button21.setStyleSheet("font-size: 14px; color: black;")
        button21.clicked.connect(lambda:self.on_click(button21))
        
        button22 = QPushButton('χ', self)
        button22.setStyleSheet("font-size: 14px; color: black;")
        button22.clicked.connect(lambda:self.on_click(button22))

        button23 = QPushButton('ψ', self)
        button23.setStyleSheet("font-size: 14px; color: black;")
        button23.clicked.connect(lambda:self.on_click(button23))
        
        button24 = QPushButton('ω', self)
        button24.setStyleSheet("font-size: 14px; color: black;")
        button24.clicked.connect(lambda:self.on_click(button24))
        
        button25 = QPushButton('Λ', self)
        button25.setStyleSheet("font-size: 14px; color: black;")
        button25.clicked.connect(lambda:self.on_click(button25))


        #----- Botones Para los Caracteres Especiales de las Variables -----
        button26 = QPushButton('[', self)
        button26.setStyleSheet("font-size: 14px; color: black;")
        button26.clicked.connect(lambda:self.on_click(button26))

        button27 = QPushButton(']', self)
        button27.setStyleSheet("font-size: 14px; color: black;")
        button27.clicked.connect(lambda:self.on_click(button27))

        button28 = QPushButton('.', self)
        button28.setStyleSheet("font-size: 14px; color: black;")
        button28.clicked.connect(lambda:self.on_click(button28))

        button29 = QPushButton('<', self)
        button29.setStyleSheet("font-size: 14px; color: black;")
        button29.clicked.connect(lambda:self.on_click(button29))

        button30 = QPushButton('>', self)
        button30.setStyleSheet("font-size: 14px; color: black;")
        button30.clicked.connect(lambda:self.on_click(button30))

        # Pertenece a las Variables 
        button31 = QPushButton('_', self)
        button31.setStyleSheet("font-size: 14px; color: black;")
        button31.clicked.connect(lambda:self.on_click(button31))

        button32 = QPushButton('(', self)
        button32.setStyleSheet("font-size: 14px; color: black;")
        button32.clicked.connect(lambda:self.on_click(button32))

        button33 = QPushButton(')', self)
        button33.setStyleSheet("font-size: 14px; color: black;")
        button33.clicked.connect(lambda:self.on_click(button33))

        button34 = QPushButton('%', self)
        button34.setStyleSheet("font-size: 14px; color: black;")
        button34.clicked.connect(lambda:self.on_click(button34))

        button35 = QPushButton('"', self)
        button35.setStyleSheet("font-size: 14px; color: black;")
        button35.clicked.connect(lambda:self.on_click(button35))

        button36 = QPushButton('/', self)
        button36.setStyleSheet("font-size: 14px; color: black;")
        button36.clicked.connect(lambda:self.on_click(button36))
        
        button37 = QPushButton('->', self)
        button37.setStyleSheet("font-size: 14px; color: black;")
        button37.clicked.connect(lambda:self.on_click(button37))

        #----- Agregar los Botones de los Caracteres Especiales de los Marcadores al Layout -----
        layoutMarker.addWidget(button,0,0) 
        layoutMarker.addWidget(button1,0,1) 
        layoutMarker.addWidget(button2,0,2) 
        layoutMarker.addWidget(button3,1,0) 
        layoutMarker.addWidget(button4,1,1) 
        layoutMarker.addWidget(button5,1,2) 
        layoutMarker.addWidget(button6,2,0) 
        layoutMarker.addWidget(button7,2,1) 
        layoutMarker.addWidget(button8,2,2)
        layoutMarker.addWidget(button9,3,0) 
        layoutMarker.addWidget(button10,3,1) 
        layoutMarker.addWidget(button11,3,2)
        layoutMarker.addWidget(button12,4,0) 
        layoutMarker.addWidget(button13,4,1) 
        layoutMarker.addWidget(button14,4,2)
        layoutMarker.addWidget(button15,5,0) 
        layoutMarker.addWidget(button16,5,1) 
        layoutMarker.addWidget(button17,5,2)
        layoutMarker.addWidget(button18,6,0) 
        layoutMarker.addWidget(button19,6,1) 
        layoutMarker.addWidget(button20,6,2)
        layoutMarker.addWidget(button21,7,0) 
        layoutMarker.addWidget(button22,7,1) 
        layoutMarker.addWidget(button23,7,2)
        layoutMarker.addWidget(button24,8,0) 
        layoutMarker.addWidget(button25,8,1) 


        #----- Agregar los Botones de los Caracteres Especiales de las Variables al Layout  -----
        layout.addWidget(button26,0,0) 
        layout.addWidget(button27,0,1) 
        layout.addWidget(button28,0,2)
        layout.addWidget(button29,1,0) 
        layout.addWidget(button30,1,1)
        layout.addWidget(button31,1,2) 
        layout.addWidget(button32,2,0) 
        layout.addWidget(button33,2,1)
        layout.addWidget(button34,2,2)  
        layout.addWidget(button35,3,0) 
        layout.addWidget(button36,3,1)
        layout.addWidget(button37,3,2) 


        #----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        horizontalGroupBoxMarker.setLayout(layoutMarker)
        horizontalGroupBox.setLayout(layout)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(horizontalGroupBoxMarker)
        windowLayout.addWidget(horizontalGroupBox)
        self.setLayout(windowLayout)


    #----- Funcion para los Botones de la Ventana Caracteres -----
    def on_click(self, caracter):

        #Pregunta  el tipo del QWidget para realizae la extracion del texto de una forma correcta
        if isinstance(self.parent.varQLineEdit, QLineEdit):
            text = self.parent.varQLineEdit.text()
        else:
            if isinstance(self.parent.varQLineEdit, QTextEdit):
                text = self.parent.varQLineEdit.toPlainText()

        newText = text + caracter.text()
        self.parent.varQLineEdit.setText(newText)

