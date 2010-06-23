# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../src/gui/SendCommandPool_PROD.ui'
#
# Created: Mon Apr 12 11:59:56 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SendCommandPool(object):
    def setupUi(self, SendCommandPool):
        SendCommandPool.setObjectName("SendCommandPool")
        SendCommandPool.setWindowModality(QtCore.Qt.WindowModal)
        SendCommandPool.resize(640, 580)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Bubble-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SendCommandPool.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(SendCommandPool)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(SendCommandPool)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pteCommand = QtGui.QPlainTextEdit(SendCommandPool)
        self.pteCommand.setObjectName("pteCommand")
        self.verticalLayout.addWidget(self.pteCommand)
        self.label_3 = QtGui.QLabel(SendCommandPool)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.bookmarks = QtGui.QComboBox(SendCommandPool)
        self.bookmarks.setObjectName("bookmarks")
        self.verticalLayout.addWidget(self.bookmarks)
        self.label_2 = QtGui.QLabel(SendCommandPool)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.glServers = QtGui.QGridLayout()
        self.glServers.setObjectName("glServers")
        self.verticalLayout.addLayout(self.glServers)
        self.buttonBox = QtGui.QDialogButtonBox(SendCommandPool)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SendCommandPool)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SendCommandPool.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SendCommandPool.reject)
        QtCore.QMetaObject.connectSlotsByName(SendCommandPool)

    def retranslateUi(self, SendCommandPool):
        SendCommandPool.setWindowTitle(QtGui.QApplication.translate("SendCommandPool", "Send a command to servers", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SendCommandPool", "Command :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SendCommandPool", "Bookmarks :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SendCommandPool", "Choose the servers :", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc
