# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../src/gui/SendCommand_PROD.ui'
#
# Created: Mon Apr 12 11:59:56 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SendCommand(object):
    def setupUi(self, SendCommand):
        SendCommand.setObjectName("SendCommand")
        SendCommand.setWindowModality(QtCore.Qt.WindowModal)
        SendCommand.resize(640, 440)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Bubble-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SendCommand.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(SendCommand)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(SendCommand)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pteCommand = QtGui.QPlainTextEdit(SendCommand)
        self.pteCommand.setObjectName("pteCommand")
        self.verticalLayout.addWidget(self.pteCommand)
        self.label_2 = QtGui.QLabel(SendCommand)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.bookmarks = QtGui.QComboBox(SendCommand)
        self.bookmarks.setObjectName("bookmarks")
        self.verticalLayout.addWidget(self.bookmarks)
        self.label_3 = QtGui.QLabel(SendCommand)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.cbLoginPass = QtGui.QComboBox(SendCommand)
        self.cbLoginPass.setObjectName("cbLoginPass")
        self.verticalLayout.addWidget(self.cbLoginPass)
        self.buttonBox = QtGui.QDialogButtonBox(SendCommand)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SendCommand)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SendCommand.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SendCommand.reject)
        QtCore.QMetaObject.connectSlotsByName(SendCommand)

    def retranslateUi(self, SendCommand):
        SendCommand.setWindowTitle(QtGui.QApplication.translate("SendCommand", "Send a command to the server", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SendCommand", "Command :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SendCommand", "Bookmarks :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SendCommand", "Login and password to use :", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc
