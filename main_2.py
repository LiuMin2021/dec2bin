#!/usr/bin/env python3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QToolTip, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QDialog, QLineEdit, QGridLayout, QFormLayout,QTextEdit,QRadioButton, QCheckBox, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer

# Klasse für das Hauptfenster
class MyWindow(QMainWindow):
    def __init__(self):# Slider + Label Anzeige Dezimalwert
        # Konstruktor von QMainWindow aufrufen
        super().__init__()
    
        self.setMinimumSize(QSize(500, 400))   
        self.setWindowTitle('Dezimal-Binär-Rechner') 
        self.setStyleSheet("background-color: rgb(1, 22, 200)")        
        wid = QWidget(self) 
        self.setCentralWidget(wid)
        
        vlayout = QVBoxLayout() #A QVBoxLayout lays out widgets in a vertical column, from top to bottom
        wid.setLayout(vlayout)
        
        self.lcd_number = QLCDNumber(2, wid) #LCD Nummber
        vlayout.addWidget(self.lcd_number)
        
        hlayout = QHBoxLayout() #widgets
        vlayout.addLayout(hlayout)
            
        # Slider + Label Anzeige Dezimalwert ,  Layout(sliderbox)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(15)
        self.slider.setSingleStep(1)
        self.slider.setValue(5)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        vlayout.addWidget(self.slider)
        
        self.label = QLabel('0')  
        self.label.setAlignment(Qt.AlignCenter)
        vlayout.addWidget(self.label)
                 
        self.slider.valueChanged[int].connect(self.dec2bin)
        self.setLayout(vlayout)
        sliderbox = QHBoxLayout()
        sliderbox.addWidget(self.slider)
        sliderbox.addWidget(self.label)
        

        # Labels fuer 4 Bits , Layout(bitbox)
        self.bitlabels = [QLabel("8"),QLabel("4"),QLabel("2"),QLabel("1")] # Liste 
        # hier bitlabels erstellen      
        bitbox = QHBoxLayout()
        for bitlabel in self.bitlabels:
            bitbox.addWidget(bitlabel)

        # Layout zusammenbauen
        vbox = QVBoxLayout()
        vbox.addLayout(sliderbox)
        vbox.addLayout(bitbox)

        # vbox anzeigen in QWidget
        self.setLayout(vbox)
        
    def dec2bin(self):
        self.label.setText(str(value))    
   

app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
