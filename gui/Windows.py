# -*- coding: utf-8 -*-
'''
Created on 04/04/2012

@author: Charly

Clases de Ventanas de la intefaz gráfica.
'''

from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    '''
    Ventana Principal de la aplicación.
    ''' 
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUi()
        
    def initUi(self):
        self.setStatusBar(StatusBar())
        self.setGeometry(0,0,800,600)
        self.center()
        self.setWindowTitle("SCLP Sistema de Control Logistico Promorutas v0.01")
        self.setWindowIcon(QtGui.QIcon('gui/icon.png'))
        self.show()
        
    def center(self):
        frameGem = self.frameGeometry()
        centre = QtGui.QDesktopWidget().availableGeometry().center()
        frameGem.moveCenter(centre)
        self.move(frameGem.topLeft()) 
        
class StatusBar(QtGui.QStatusBar):
    '''
    Barra de Estado Principal
    '''
    def __init__(self):
        super(StatusBar, self).__init__()       