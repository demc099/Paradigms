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

    def createGridLayout(self):    
        horizontalGroupBox = QGroupBox()

        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
 
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
        
        layout.addWidget(button,0,0) 
        layout.addWidget(button1,0,1) 
        layout.addWidget(button2,0,2) 
        layout.addWidget(button3,1,0) 
        layout.addWidget(button4,1,1) 
        layout.addWidget(button5,1,2) 
        layout.addWidget(button6,2,0) 
        layout.addWidget(button7,2,1) 
        layout.addWidget(button8,2,2)
        layout.addWidget(button9,3,0) 
        layout.addWidget(button10,3,1) 
        layout.addWidget(button11,3,2)
        layout.addWidget(button12,4,0) 
        layout.addWidget(button13,4,1) 
        layout.addWidget(button14,4,2)
        layout.addWidget(button15,5,0) 
        layout.addWidget(button16,5,1) 
        layout.addWidget(button17,5,2)
        layout.addWidget(button18,6,0) 
        layout.addWidget(button19,6,1) 
        layout.addWidget(button20,6,2)
        layout.addWidget(button21,7,0) 
        layout.addWidget(button22,7,1) 
        layout.addWidget(button23,7,2)
        layout.addWidget(button24,8,0) 
        layout.addWidget(button25,8,1) 

        horizontalGroupBox.setLayout(layout)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(horizontalGroupBox)
        self.setLayout(windowLayout)

    def on_click(self, caracter):
        texto = self.parent.markersEdit.text()
        nuevoTexto = texto + caracter.text()
        self.parent.markersEdit.setText(nuevoTexto)