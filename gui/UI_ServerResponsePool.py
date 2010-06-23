# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../src/gui/ServerResponsePool_PROD.ui'
#
# Created: Mon Apr 12 12:00:00 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ServerResponsePool(object):
    def setupUi(self, ServerResponsePool):
        ServerResponsePool.setObjectName("ServerResponsePool")
        ServerResponsePool.setWindowModality(QtCore.Qt.WindowModal)
        ServerResponsePool.resize(660, 165)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Bubble-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ServerResponsePool.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(ServerResponsePool)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pteCommandReminder = QtGui.QPlainTextEdit(ServerResponsePool)
        self.pteCommandReminder.setMinimumSize(QtCore.QSize(0, 50))
        self.pteCommandReminder.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pteCommandReminder.setReadOnly(True)
        self.pteCommandReminder.setObjectName("pteCommandReminder")
        self.verticalLayout.addWidget(self.pteCommandReminder)
        self.label = QtGui.QLabel(ServerResponsePool)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.addLayout(self.gridLayout)
        self.bookmark = QtGui.QCheckBox(ServerResponsePool)
        self.bookmark.setObjectName("bookmark")
        self.verticalLayout.addWidget(self.bookmark)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbSendAnOtherCommand = QtGui.QPushButton(ServerResponsePool)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/Left_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbSendAnOtherCommand.setIcon(icon1)
        self.pbSendAnOtherCommand.setObjectName("pbSendAnOtherCommand")
        self.horizontalLayout.addWidget(self.pbSendAnOtherCommand)
        self.buttonBox = QtGui.QDialogButtonBox(ServerResponsePool)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ServerResponsePool)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ServerResponsePool.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ServerResponsePool.reject)
        QtCore.QMetaObject.connectSlotsByName(ServerResponsePool)

    def retranslateUi(self, ServerResponsePool):
        ServerResponsePool.setWindowTitle(QtGui.QApplication.translate("ServerResponsePool", "Servers responses", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ServerResponsePool", "Servers Responses :", None, QtGui.QApplication.UnicodeUTF8))
        self.bookmark.setText(QtGui.QApplication.translate("ServerResponsePool", "Bookmark this command", None, QtGui.QApplication.UnicodeUTF8))
        self.pbSendAnOtherCommand.setText(QtGui.QApplication.translate("ServerResponsePool", "Send an other command", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc
