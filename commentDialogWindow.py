# -*- coding: utf-8 -*-
"""
Created on Tue Dec 02 15:16:27 2014

@author: dvalovcin
"""

from PyQt4 import QtGui, QtCore
import re
from commentDialog_ui import Ui_Comment




class CommentDialogBox(QtGui.QDialog):
    def __init__(self, parent=None, currentNames=None, currentComment = None):
        super(CommentDialogBox, self).__init__(parent)
        self.ui=Ui_Comment()
        self.ui.setupUi(self)
        if not currentNames == None:
            self.ui.CH1Name.setText(currentNames[0])
            self.ui.CH2Name.setText(currentNames[1])
            self.ui.CH3Name.setText(currentNames[2])
            self.ui.CH4Name.setText(currentNames[3])
        if not currentComment == None:
            self.ui.headerText.setPlainText(currentComment)
        
    @staticmethod
    def getComments(currentNames, currentComment, parent=None):
        dialog = CommentDialogBox(parent, currentNames, currentComment)
        result = dialog.exec_()
        return ([str(dialog.ui.CH1Name.text()), str(dialog.ui.CH2Name.text()), 
                 str(dialog.ui.CH3Name.text()), str(dialog.ui.CH4Name.text()) ], 
                 str(dialog.ui.headerText.toPlainText()), result == QtGui.QDialog.Accepted)
































