# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Darren\Python\Osc\V2\mainWindow.ui'
#
# Created: Mon Dec 01 16:41:02 2014
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
        MainWindow.resize(900, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pw1 = PlotWidget(self.centralwidget)
        self.pw1.setObjectName(_fromUtf8("pw1"))
        self.horizontalLayout.addWidget(self.pw1)
        self.pw2 = PlotWidget(self.centralwidget)
        self.pw2.setObjectName(_fromUtf8("pw2"))
        self.horizontalLayout.addWidget(self.pw2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.BoundaryValuesBox = QtGui.QGridLayout()
        self.BoundaryValuesBox.setObjectName(_fromUtf8("BoundaryValuesBox"))
        self.verticalLayout.addLayout(self.BoundaryValuesBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setCheckable(True)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.horizontalLayout_2.addWidget(self.startButton)
        self.compareButton = QtGui.QPushButton(self.centralwidget)
        self.compareButton.setObjectName(_fromUtf8("compareButton"))
        self.horizontalLayout_2.addWidget(self.compareButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_CHA = QtGui.QMenu(self.menubar)
        self.menu_CHA.setObjectName(_fromUtf8("menu_CHA"))
        self.menu_CHB = QtGui.QMenu(self.menubar)
        self.menu_CHB.setObjectName(_fromUtf8("menu_CHB"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.file_EditComments = QtGui.QAction(MainWindow)
        self.file_EditComments.setObjectName(_fromUtf8("file_EditComments"))
        self.file_queryScope = QtGui.QAction(MainWindow)
        self.file_queryScope.setObjectName(_fromUtf8("file_queryScope"))
        self.CHA_setCH1 = QtGui.QAction(MainWindow)
        self.CHA_setCH1.setCheckable(True)
        self.CHA_setCH1.setChecked(True)
        self.CHA_setCH1.setObjectName(_fromUtf8("CHA_setCH1"))
        self.CHA_setCH2 = QtGui.QAction(MainWindow)
        self.CHA_setCH2.setCheckable(True)
        self.CHA_setCH2.setChecked(False)
        self.CHA_setCH2.setEnabled(False)
        self.CHA_setCH2.setObjectName(_fromUtf8("CHA_setCH2"))
        self.CHA_setCH3 = QtGui.QAction(MainWindow)
        self.CHA_setCH3.setCheckable(True)
        self.CHA_setCH3.setEnabled(False)
        self.CHA_setCH3.setObjectName(_fromUtf8("CHA_setCH3"))
        self.CHA_setCH4 = QtGui.QAction(MainWindow)
        self.CHA_setCH4.setCheckable(True)
        self.CHA_setCH4.setEnabled(False)
        self.CHA_setCH4.setObjectName(_fromUtf8("CHA_setCH4"))
        self.menu_File.addAction(self.file_EditComments)
        self.menu_File.addAction(self.file_queryScope)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_CHA.menuAction())
        self.menubar.addAction(self.menu_CHB.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "TDS2014 Boxcar Integrator", None))
        self.startButton.setText(_translate("MainWindow", "Start Collection", None))
        self.compareButton.setText(_translate("MainWindow", "Plot Versus", None))
        self.saveButton.setText(_translate("MainWindow", "Save Data", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menu_CHA.setTitle(_translate("MainWindow", "Channel A", None))
        self.menu_CHB.setTitle(_translate("MainWindow", "Channel B", None))
        self.file_EditComments.setText(_translate("MainWindow", "Edit Comments...", None))
        self.file_queryScope.setText(_translate("MainWindow", "Request Scope Parameters", None))
        self.CHA_setCH1.setText(_translate("MainWindow", "CH1", None))
        self.CHA_setCH2.setText(_translate("MainWindow", "CH2", None))
        self.CHA_setCH3.setText(_translate("MainWindow", "CH3", None))
        self.CHA_setCH4.setText(_translate("MainWindow", "CH4", None))

from pyqtgraph import PlotWidget
