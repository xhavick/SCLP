'''
Created on 04/04/2012

@author: Charly

Clases de Ventanas de la intefaz gráfica.
'''

from PyQt4 import QtGui

class MainWindow(QtGui.QWidget):
    '''
    Ventana Principal de la aplicación.
    ''' 
    def __init__(self):
        QtGui.QWidget.__init__()
        self.initUi()
        
    def initUi(self):
        pass
        
        