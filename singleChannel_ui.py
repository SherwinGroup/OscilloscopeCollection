# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dvalovcin\Documents\GitHub\OscilloscopeCollection\singleChannel.ui'
#
# Created: Wed Mar 18 08:43:10 2015
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

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(556, 447)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.graphicsView = QtGui.QGraphicsView(Frame)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_2 = QtGui.QGroupBox(Frame)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tBGEnd = QFNumberEdit(self.groupBox_2)
        self.tBGEnd.setObjectName(_fromUtf8("tBGEnd"))
        self.horizontalLayout_2.addWidget(self.tBGEnd)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(Frame)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tBGStart = QFNumberEdit(self.groupBox)
        self.tBGStart.setObjectName(_fromUtf8("tBGStart"))
        self.horizontalLayout.addWidget(self.tBGStart)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(Frame)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tSGStart = QFNumberEdit(self.groupBox_3)
        self.tSGStart.setObjectName(_fromUtf8("tSGStart"))
        self.horizontalLayout_3.addWidget(self.tSGStart)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(Frame)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tSGEnd = QFNumberEdit(self.groupBox_4)
        self.tSGEnd.setObjectName(_fromUtf8("tSGEnd"))
        self.horizontalLayout_4.addWidget(self.tSGEnd)
        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.bInit = QtGui.QPushButton(Frame)
        self.bInit.setObjectName(_fromUtf8("bInit"))
        self.gridLayout.addWidget(self.bInit, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.groupBox_2.setTitle(_translate("Frame", "BG End", None))
        self.groupBox.setTitle(_translate("Frame", "BG Start", None))
        self.groupBox_3.setTitle(_translate("Frame", "Sig Start", None))
        self.groupBox_4.setTitle(_translate("Frame", "Sig End", None))
        self.bInit.setText(_translate("Frame", "Initialize", None))

from InstsAndQt.customQt import QFNumberEdit
