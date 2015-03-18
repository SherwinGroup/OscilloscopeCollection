# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 15:36:27 2014

@author: Darren
"""

from PyQt4 import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import threading
from mainWindow_ui import Ui_MainWindow
import datetime
import re

class Win(QtGui.QMainWindow):
    boxCarPairsSignal = QtCore.pyqtSignal(dict)
    settings = dict()
    parentSettingsSignal = QtCore.pyqtSignal(dict)
    
    def __init__(self):
        super(Win,self).__init__()
        self.initUI()
        
    def initUI(self):
        #Import ui file from designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  

        self.show()
        
    def closeEvent(self,event):
        self.close()
        

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    ex = Win()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()