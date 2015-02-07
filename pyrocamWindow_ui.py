# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Darren\Python\Pyrocam\Testing\pyrocamWindow.ui'
#
# Created: Tue Jan 13 12:39:38 2015
#      by: PyQt4 UI code generator 4.11.3
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
        MainWindow.resize(732, 562)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_rawPyro = QtGui.QWidget()
        self.tab_rawPyro.setObjectName(_fromUtf8("tab_rawPyro"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_rawPyro)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.rawPyro = ImageView(self.tab_rawPyro)
        self.rawPyro.setObjectName(_fromUtf8("rawPyro"))
        self.horizontalLayout_2.addWidget(self.rawPyro)
        self.tabWidget.addTab(self.tab_rawPyro, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.button1 = QtGui.QPushButton(self.centralwidget)
        self.button1.setObjectName(_fromUtf8("button1"))
        self.horizontalLayout.addWidget(self.button1)
        self.button2 = QtGui.QPushButton(self.centralwidget)
        self.button2.setObjectName(_fromUtf8("button2"))
        self.horizontalLayout.addWidget(self.button2)
        self.button3 = QtGui.QPushButton(self.centralwidget)
        self.button3.setObjectName(_fromUtf8("button3"))
        self.horizontalLayout.addWidget(self.button3)
        self.button4 = QtGui.QPushButton(self.centralwidget)
        self.button4.setObjectName(_fromUtf8("button4"))
        self.horizontalLayout.addWidget(self.button4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rawPyro), _translate("MainWindow", "Raw Pyro", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page", None))
        self.button1.setText(_translate("MainWindow", "PushButton", None))
        self.button2.setText(_translate("MainWindow", "PushButton", None))
        self.button3.setText(_translate("MainWindow", "PushButton", None))
        self.button4.setText(_translate("MainWindow", "PushButton", None))

from pyqtgraph import ImageView
