# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../src/gui/ServerResponse.ui'
#
# Created: Mon Apr 12 11:59:57 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ServerResponse(object):
    def setupUi(self, ServerResponse):
        ServerResponse.setObjectName("ServerResponse")
        ServerResponse.setWindowModality(QtCore.Qt.WindowModal)
        ServerResponse.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Bubble-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ServerResponse.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(ServerResponse)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pteCommandReminder = QtGui.QPlainTextEdit(ServerResponse)
        self.pteCommandReminder.setMinimumSize(QtCore.QSize(0, 50))
        self.pteCommandReminder.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pteCommandReminder.setReadOnly(True)
        self.pteCommandReminder.setObjectName("pteCommandReminder")
        self.verticalLayout.addWidget(self.pteCommandReminder)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(ServerResponse)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pbCopy = QtGui.QPushButton(ServerResponse)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCopy.setIcon(icon1)
        self.pbCopy.setObjectName("pbCopy")
        self.horizontalLayout_2.addWidget(self.pbCopy)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.response = QtGui.QPlainTextEdit(ServerResponse)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.response.setFont(font)
        self.response.setReadOnly(True)
        self.response.setObjectName("response")
        self.verticalLayout.addWidget(self.response)
        self.bookmark = QtGui.QCheckBox(ServerResponse)
        self.bookmark.setObjectName("bookmark")
        self.verticalLayout.addWidget(self.bookmark)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pbSendAnOtherCommand = QtGui.QPushButton(ServerResponse)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/Left_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbSendAnOtherCommand.setIcon(icon2)
        self.pbSendAnOtherCommand.setObjectName("pbSendAnOtherCommand")
        self.horizontalLayout.addWidget(self.pbSendAnOtherCommand)
        self.buttonBox = QtGui.QDialogButtonBox(ServerResponse)
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

        self.retranslateUi(ServerResponse)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ServerResponse.accept)
        QtCore.QObject.connect(self.pbCopy, QtCore.SIGNAL("pressed()"), self.response.selectAll)
        QtCore.QObject.connect(self.pbCopy, QtCore.SIGNAL("released()"), self.response.copy)
        QtCore.QMetaObject.connectSlotsByName(ServerResponse)

    def retranslateUi(self, ServerResponse):
        ServerResponse.setWindowTitle(QtGui.QApplication.translate("ServerResponse", "Server response", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ServerResponse", "Server Response :", None, QtGui.QApplication.UnicodeUTF8))
        self.pbCopy.setToolTip(QtGui.QApplication.translate("ServerResponse", "Copy response to clipboard.", None, QtGui.QApplication.UnicodeUTF8))
        self.bookmark.setText(QtGui.QApplication.translate("ServerResponse", "Bookmark this command", None, QtGui.QApplication.UnicodeUTF8))
        self.pbSendAnOtherCommand.setText(QtGui.QApplication.translate("ServerResponse", "Send an other command", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc
