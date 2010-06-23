# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../src/gui/BookmarkCommandWindow.ui'
#
# Created: Mon Apr 12 12:00:01 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_BookmarkCommandWindow(object):
    def setupUi(self, BookmarkCommandWindow):
        BookmarkCommandWindow.setObjectName("BookmarkCommandWindow")
        BookmarkCommandWindow.setWindowModality(QtCore.Qt.WindowModal)
        BookmarkCommandWindow.resize(640, 340)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Bubble-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BookmarkCommandWindow.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(BookmarkCommandWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(BookmarkCommandWindow)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.description = QtGui.QPlainTextEdit(BookmarkCommandWindow)
        self.description.setMaximumSize(QtCore.QSize(16777215, 100))
        self.description.setObjectName("description")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.description)
        self.command = QtGui.QPlainTextEdit(BookmarkCommandWindow)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.command.setFont(font)
        self.command.setObjectName("command")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.command)
        self.label_2 = QtGui.QLabel(BookmarkCommandWindow)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(BookmarkCommandWindow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(BookmarkCommandWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), BookmarkCommandWindow.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), BookmarkCommandWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(BookmarkCommandWindow)

    def retranslateUi(self, BookmarkCommandWindow):
        BookmarkCommandWindow.setWindowTitle(QtGui.QApplication.translate("BookmarkCommandWindow", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("BookmarkCommandWindow", "Description :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("BookmarkCommandWindow", "Command :", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc
