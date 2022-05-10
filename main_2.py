#!/usr/bin/env python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer
from gpiozero import LED, LEDBoard
from signal import pause


# Klasse für das Hauptfenster
class MyWindow(QMainWindow):
    def __init__(self):# Slider + Label Anzeige Dezimalwert
        # Konstruktor von QMainWindow aufrufen
        super().__init__()
        
        self.leds = LEDBoard(18, 23, 24, 25)
        self.setMinimumSize(QSize(500, 300))   
        self.setWindowTitle('Dezimal-Binär-Rechner') 
        self.setStyleSheet("background-color: rgb(1, 22, 200)")        
        wid = QWidget(self) 
        self.setCentralWidget(wid)
        
        vlayout = QVBoxLayout() #A QVBoxLayout lays out widgets in a vertical column, from top to bottom
        wid.setLayout(vlayout)
        
        self.lcd_number = QLCDNumber(2, wid) #LCD Nummber
        vlayout.addWidget(self.lcd_number)
        
                   
        # Slider + Label Anzeige Dezimalwert ,  Layout(sliderbox)
        self.slider = QSlider(Qt.Horizontal,wid)
        self.slider.setMinimum(0)
        self.slider.setMaximum(15)
        #self.slider.setSingleStep(1)
        self.slider.setValue(5)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        #vlayout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.dec2bin)
        
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
        self.length=len(self.bitlabels)
        print (self.length)
        
        # hier bitlabels erstellen      
        bitbox = QHBoxLayout()
        
       

        # Layout zusammenbauen
        vbox = QVBoxLayout()
        vbox.addLayout(sliderbox)
        vbox.addLayout(bitbox)

        # vbox anzeigen in QWidget
        self.setLayout(vbox)
        
        for index, bitlabel in enumerate(self.bitlabels):
            bitbox.addWidget(bitlabel)            
            bitlabel.setStyleSheet("background-color: rgb(100, 100, 100)")
            bitlabel.setFixedWidth(20)
            bitlabel.setFixedHeight(20)
            bitlabel.setAlignment(Qt.AlignCenter)
        
    def dec2bin(self,value):
        self.label.setText(str(value)) 
        for j in range(self.length):
            print (j)
            if (value & 1<<j):        
                self.bitlabels[self.length-1-j].setStyleSheet("background-color: rgb(255, 0, 0)")
                self.leds[j].on()            
            else:
                self.bitlabels[self.length-1-j].setStyleSheet("background-color: rgb(100, 100, 100)")
                self.leds[j].off() 
   

app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()

