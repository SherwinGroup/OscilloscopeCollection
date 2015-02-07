# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 14:29:19 2015

@author: dvalovcin
"""

import numpy as np
import matplotlib.pylab as plt
import win32com.client
from pyrocamWindow_ui import Ui_MainWindow
from PyQt4 import QtGui, QtCore
import pyqtgraph as pg
import time
import threading
import pythoncom


class PyroWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(PyroWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.show()
        self.runFlag = True
        pythoncom.CoInitialize()
        self.pyro = win32com.client.Dispatch('PyrocamIIIActiveX.PyrocamIIIActiveX')
        self.pyro.Open()
        parent.updatePyro.connect(self.singleUpdate)
        
    def startPyro(self):
        try:
            pythoncom.CoInitialize()
            self.pyro = win32com.client.Dispatch('PyrocamIIIActiveX.PyrocamIIIActiveX')
            self.pyro.Open()
        except: 
            print 'Error opening pyrocam channel!'
        
    def singleUpdate(self):
        print 'update1'
#        self.pyro.Start()
        print 'update2'
        data = np.array(self.pyro.Data).T
        print 'update3'
        self.ui.rawPyro.setImage(np.array(data))
        
        
            
class debugWin(QtGui.QMainWindow):
    updatePyro = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(debugWin,self).__init__()
        vlayout = QtGui.QVBoxLayout()
        self.button_launch = QtGui.QPushButton('Launch window', self)
        self.button_launch.move(50, 30)
        self.button_collect = QtGui.QPushButton('Update Data', self)
        self.button_collect.move(150, 30)
        
        self.button_launch.clicked.connect(self.launch)
        self.button_collect.clicked.connect(self.requestUpdate)
        
        vlayout.addWidget(self.button_launch)
        vlayout.addWidget(self.button_collect)
#        self.setLayout(vlayout)
        self.show()
        
        
    def launch(self):
        self.button_launch.setEnabled(False)
        self.pyro = PyroWindow(self)
        #self.pyro.show()
    
    def requestUpdate(self):
        self.updatePyro.emit()
        
        

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    ex = debugWin()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
    
    
img = pg.gaussianFilter(np.random.normal(size=(200, 200)), (5, 5)) * 20 + 100
img = img[np.newaxis,:,:]
decay = np.exp(-np.linspace(0,0.3,100))[:,np.newaxis,np.newaxis]
data = np.random.normal(size=(100, 200, 200))
data += img * decay
data += 2