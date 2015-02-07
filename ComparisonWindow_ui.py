# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Darren\Python\Osc\ComparisonWindow.ui'
#
# Created: Tue Oct 07 10:37:31 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.collectButton = QtGui.QPushButton(self.centralwidget)
        self.collectButton.setCheckable(True)
        self.collectButton.setObjectName(_fromUtf8("collectButton"))
        self.horizontalLayout.addWidget(self.collectButton)
        self.resetButton = QtGui.QPushButton(self.centralwidget)
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.horizontalLayout.addWidget(self.resetButton)
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.collectButton.setText(_translate("MainWindow", "Collect Data", None))
        self.resetButton.setText(_translate("MainWindow", "Reset Data", None))
        self.saveButton.setText(_translate("MainWindow", "Save Data", None))

from pyqtgraph import PlotWidget
