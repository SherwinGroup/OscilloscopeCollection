# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Darren\Python\Osc\V2\commentDialog.ui'
#
# Created: Thu Dec 04 17:47:49 2014
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

class Ui_Comment(object):
    def setupUi(self, Comment):
        Comment.setObjectName(_fromUtf8("Comment"))
        Comment.resize(394, 480)
        self.horizontalLayout_6 = QtGui.QHBoxLayout(Comment)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Comment)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.CH1Name = QtGui.QLineEdit(Comment)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH1Name.sizePolicy().hasHeightForWidth())
        self.CH1Name.setSizePolicy(sizePolicy)
        self.CH1Name.setObjectName(_fromUtf8("CH1Name"))
        self.horizontalLayout.addWidget(self.CH1Name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Comment)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.CH2Name = QtGui.QLineEdit(Comment)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH2Name.sizePolicy().hasHeightForWidth())
        self.CH2Name.setSizePolicy(sizePolicy)
        self.CH2Name.setObjectName(_fromUtf8("CH2Name"))
        self.horizontalLayout_2.addWidget(self.CH2Name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(Comment)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.CH3Name = QtGui.QLineEdit(Comment)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH3Name.sizePolicy().hasHeightForWidth())
        self.CH3Name.setSizePolicy(sizePolicy)
        self.CH3Name.setObjectName(_fromUtf8("CH3Name"))
        self.horizontalLayout_3.addWidget(self.CH3Name)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(Comment)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.CH4Name = QtGui.QLineEdit(Comment)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH4Name.sizePolicy().hasHeightForWidth())
        self.CH4Name.setSizePolicy(sizePolicy)
        self.CH4Name.setObjectName(_fromUtf8("CH4Name"))
        self.horizontalLayout_4.addWidget(self.CH4Name)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(Comment)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_5.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.label_5 = QtGui.QLabel(Comment)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.headerText = QtGui.QPlainTextEdit(Comment)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.headerText.sizePolicy().hasHeightForWidth())
        self.headerText.setSizePolicy(sizePolicy)
        self.headerText.setObjectName(_fromUtf8("headerText"))
        self.verticalLayout_2.addWidget(self.headerText)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.retranslateUi(Comment)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Comment.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Comment.reject)
        QtCore.QMetaObject.connectSlotsByName(Comment)

    def retranslateUi(self, Comment):
        Comment.setWindowTitle(_translate("Comment", "Edit Comments", None))
        self.label.setText(_translate("Comment", "CH1 Name:", None))
        self.CH1Name.setText(_translate("Comment", "CH1", None))
        self.label_2.setText(_translate("Comment", "CH2 Name:", None))
        self.CH2Name.setText(_translate("Comment", "CH2", None))
        self.label_3.setText(_translate("Comment", "CH3 Name:", None))
        self.CH3Name.setText(_translate("Comment", "CH3", None))
        self.label_4.setText(_translate("Comment", "CH4 Name:", None))
        self.CH4Name.setText(_translate("Comment", "CH4", None))
        self.label_5.setText(_translate("Comment", "Comments for save files:", None))
        self.headerText.setPlainText(_translate("Comment", "{DATE}", None))

