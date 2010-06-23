# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../src/gui/EditLoginPassWindow_PROD.ui'
#
# Created: Mon Apr 12 11:59:55 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditLoginPassWindow(object):
    def setupUi(self, EditLoginPassWindow):
        EditLoginPassWindow.setObjectName("EditLoginPassWindow")
        EditLoginPassWindow.setWindowModality(QtCore.Qt.WindowModal)
        EditLoginPassWindow.resize(700, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Key-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditLoginPassWindow.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(EditLoginPassWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lwLoginPass = QtGui.QListWidget(EditLoginPassWindow)
        self.lwLoginPass.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lwLoginPass.setObjectName("lwLoginPass")
        self.verticalLayout.addWidget(self.lwLoginPass)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pbAddPair = QtGui.QPushButton(EditLoginPassWindow)
        self.pbAddPair.setMaximumSize(QtCore.QSize(100, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/Plus-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAddPair.setIcon(icon1)
        self.pbAddPair.setObjectName("pbAddPair")
        self.horizontalLayout_2.addWidget(self.pbAddPair)
        self.pbDelPair = QtGui.QPushButton(EditLoginPassWindow)
        self.pbDelPair.setMaximumSize(QtCore.QSize(100, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/Cross-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbDelPair.setIcon(icon2)
        self.pbDelPair.setObjectName("pbDelPair")
        self.horizontalLayout_2.addWidget(self.pbDelPair)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.GroupBox = QtGui.QGroupBox(EditLoginPassWindow)
        self.GroupBox.setObjectName("GroupBox")
        self.formLayout = QtGui.QFormLayout(self.GroupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.GroupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.leLogin = QtGui.QLineEdit(self.GroupBox)
        self.leLogin.setObjectName("leLogin")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.leLogin)
        self.label_2 = QtGui.QLabel(self.GroupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lePassword = QtGui.QLineEdit(self.GroupBox)
        self.lePassword.setObjectName("lePassword")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lePassword)
        self.buttonBox = QtGui.QDialogButtonBox(self.GroupBox)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.buttonBox)
        self.label_3 = QtGui.QLabel(self.GroupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lwDefault = QtGui.QListWidget(self.GroupBox)
        self.lwDefault.setObjectName("lwDefault")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lwDefault)
        self.horizontalLayout.addWidget(self.GroupBox)

        self.retranslateUi(EditLoginPassWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), EditLoginPassWindow.close)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), EditLoginPassWindow.accept)
        QtCore.QMetaObject.connectSlotsByName(EditLoginPassWindow)

    def retranslateUi(self, EditLoginPassWindow):
        EditLoginPassWindow.setWindowTitle(QtGui.QApplication.translate("EditLoginPassWindow", "Manage logins and passwords", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox.setTitle(QtGui.QApplication.translate("EditLoginPassWindow", "Change login or password", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditLoginPassWindow", "Login :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditLoginPassWindow", "Password :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("EditLoginPassWindow", "Default for :", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc
