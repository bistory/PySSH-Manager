# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../src/gui/ServerResponsePoolView.ui'
#
# Created: Mon Apr 12 12:00:00 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ServerResponsePoolView(object):
    def setupUi(self, ServerResponsePoolView):
        ServerResponsePoolView.setObjectName("ServerResponsePoolView")
        ServerResponsePoolView.setWindowModality(QtCore.Qt.WindowModal)
        ServerResponsePoolView.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Bubble-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ServerResponsePoolView.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(ServerResponsePoolView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.response = QtGui.QPlainTextEdit(ServerResponsePoolView)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.response.setFont(font)
        self.response.setReadOnly(True)
        self.response.setObjectName("response")
        self.verticalLayout.addWidget(self.response)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbCopy = QtGui.QPushButton(ServerResponsePoolView)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCopy.setIcon(icon1)
        self.pbCopy.setObjectName("pbCopy")
        self.horizontalLayout.addWidget(self.pbCopy)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(ServerResponsePoolView)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ServerResponsePoolView)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ServerResponsePoolView.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ServerResponsePoolView.reject)
        QtCore.QObject.connect(self.pbCopy, QtCore.SIGNAL("pressed()"), self.response.selectAll)
        QtCore.QObject.connect(self.pbCopy, QtCore.SIGNAL("released()"), self.response.copy)
        QtCore.QMetaObject.connectSlotsByName(ServerResponsePoolView)

    def retranslateUi(self, ServerResponsePoolView):
        ServerResponsePoolView.setWindowTitle(QtGui.QApplication.translate("ServerResponsePoolView", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pbCopy.setToolTip(QtGui.QApplication.translate("ServerResponsePoolView", "Copy response to clipboard.", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc
