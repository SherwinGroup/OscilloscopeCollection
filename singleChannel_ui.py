# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dvalovcin\Documents\GitHub\OscilloscopeCollection\singleChannel.ui'
#
# Created: Wed Mar 18 14:40:18 2015
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(568, 610)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gPlot = PlotWidget(Form)
        self.gPlot.setObjectName(_fromUtf8("gPlot"))
        self.verticalLayout.addWidget(self.gPlot)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tBGStart = QFNumberEdit(self.groupBox)
        self.tBGStart.setObjectName(_fromUtf8("tBGStart"))
        self.horizontalLayout.addWidget(self.tBGStart)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.bInit = QtGui.QPushButton(Form)
        self.bInit.setObjectName(_fromUtf8("bInit"))
        self.gridLayout.addWidget(self.bInit, 0, 3, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tSGEnd = QFNumberEdit(self.groupBox_4)
        self.tSGEnd.setObjectName(_fromUtf8("tSGEnd"))
        self.horizontalLayout_4.addWidget(self.tSGEnd)
        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tSGStart = QFNumberEdit(self.groupBox_3)
        self.tSGStart.setObjectName(_fromUtf8("tSGStart"))
        self.horizontalLayout_3.addWidget(self.tSGStart)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tBGEnd = QFNumberEdit(self.groupBox_2)
        self.tBGEnd.setObjectName(_fromUtf8("tBGEnd"))
        self.horizontalLayout_2.addWidget(self.tBGEnd)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(Form)
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.tBGBoxcar = QFNumberEdit(self.groupBox_5)
        self.tBGBoxcar.setObjectName(_fromUtf8("tBGBoxcar"))
        self.horizontalLayout_5.addWidget(self.tBGBoxcar)
        self.gridLayout.addWidget(self.groupBox_5, 0, 2, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(Form)
        self.groupBox_6.setEnabled(False)
        self.groupBox_6.setFlat(True)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.tSGBoxcar = QFNumberEdit(self.groupBox_6)
        self.tSGBoxcar.setObjectName(_fromUtf8("tSGBoxcar"))
        self.horizontalLayout_6.addWidget(self.tSGBoxcar)
        self.gridLayout.addWidget(self.groupBox_6, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "BG Start", None))
        self.tBGStart.setText(_translate("Form", "0", None))
        self.bInit.setText(_translate("Form", "Initialize", None))
        self.groupBox_4.setTitle(_translate("Form", "Sig End", None))
        self.tSGEnd.setText(_translate("Form", "0", None))
        self.groupBox_3.setTitle(_translate("Form", "Sig Start", None))
        self.tSGStart.setText(_translate("Form", "0", None))
        self.groupBox_2.setTitle(_translate("Form", "BG End", None))
        self.tBGEnd.setText(_translate("Form", "0", None))
        self.groupBox_5.setTitle(_translate("Form", "Value:", None))
        self.groupBox_6.setTitle(_translate("Form", "Value:", None))

from pyqtgraph import PlotWidget
from InstsAndQt.customQt import QFNumberEdit
