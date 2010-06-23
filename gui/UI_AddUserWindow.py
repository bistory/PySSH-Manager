# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../src/gui/AddUserWindow.ui'
#
# Created: Mon Apr 12 11:59:59 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddUserWindow(object):
    def setupUi(self, AddUserWindow):
        AddUserWindow.setObjectName("AddUserWindow")
        AddUserWindow.resize(320, 110)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Plus-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddUserWindow.setWindowIcon(icon)
        self.formLayout = QtGui.QFormLayout(AddUserWindow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(AddUserWindow)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.leLogin = QtGui.QLineEdit(AddUserWindow)
        self.leLogin.setObjectName("leLogin")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.leLogin)
        self.label_2 = QtGui.QLabel(AddUserWindow)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lePassword = QtGui.QLineEdit(AddUserWindow)
        self.lePassword.setObjectName("lePassword")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lePassword)
        self.buttonBox = QtGui.QDialogButtonBox(AddUserWindow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(AddUserWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AddUserWindow.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AddUserWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(AddUserWindow)

    def retranslateUi(self, AddUserWindow):
        AddUserWindow.setWindowTitle(QtGui.QApplication.translate("AddUserWindow", "Add a user", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddUserWindow", "Login :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddUserWindow", "Password :", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc
