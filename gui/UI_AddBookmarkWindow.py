# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../src/gui/AddBookmarkWindow.ui'
#
# Created: Mon Apr 12 12:00:02 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddBookmarkWindow(object):
    def setupUi(self, AddBookmarkWindow):
        AddBookmarkWindow.setObjectName("AddBookmarkWindow")
        AddBookmarkWindow.resize(330, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Plus-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddBookmarkWindow.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(AddBookmarkWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(AddBookmarkWindow)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pteCommand = QtGui.QPlainTextEdit(AddBookmarkWindow)
        self.pteCommand.setObjectName("pteCommand")
        self.verticalLayout.addWidget(self.pteCommand)
        self.label_2 = QtGui.QLabel(AddBookmarkWindow)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pteDescription = QtGui.QPlainTextEdit(AddBookmarkWindow)
        self.pteDescription.setObjectName("pteDescription")
        self.verticalLayout.addWidget(self.pteDescription)
        self.buttonBox = QtGui.QDialogButtonBox(AddBookmarkWindow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddBookmarkWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AddBookmarkWindow.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AddBookmarkWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(AddBookmarkWindow)

    def retranslateUi(self, AddBookmarkWindow):
        AddBookmarkWindow.setWindowTitle(QtGui.QApplication.translate("AddBookmarkWindow", "Add a bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddBookmarkWindow", "Command :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddBookmarkWindow", "Description :", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc
