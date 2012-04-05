# -*- coding: utf-8 -*-

'''
Created on 04/04/2012

@author: Charly
'''

import ctypes
import sys
from PyQt4 import QtGui
from gui import Windows

def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyle('Cleanlooks')
    mainWin = Windows.MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    appid = 'revolucionip.scl.sclp.01'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
    main()
else:
    print "Inicie este Archivo directamente"
    