# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../src/gui/EditServerWindow.ui'
#
# Created: Mon Apr 12 11:59:57 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditServerWindow(object):
    def setupUi(self, EditServerWindow):
        EditServerWindow.setObjectName("EditServerWindow")
        EditServerWindow.setWindowModality(QtCore.Qt.WindowModal)
        EditServerWindow.resize(640, 357)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Pencil-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditServerWindow.setWindowIcon(icon)
        self.formLayout = QtGui.QFormLayout(EditServerWindow)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(EditServerWindow)
        self.label.setMinimumSize(QtCore.QSize(184, 0))
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.leHost = QtGui.QLineEdit(EditServerWindow)
        self.leHost.setObjectName("leHost")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.leHost)
        self.label_2 = QtGui.QLabel(EditServerWindow)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.sbPort = QtGui.QSpinBox(EditServerWindow)
        self.sbPort.setMaximum(2147483647)
        self.sbPort.setProperty("value", 22)
        self.sbPort.setObjectName("sbPort")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.sbPort)
        self.label_6 = QtGui.QLabel(EditServerWindow)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.leLabel = QtGui.QLineEdit(EditServerWindow)
        self.leLabel.setObjectName("leLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.leLabel)
        self.rbUseExist = QtGui.QRadioButton(EditServerWindow)
        self.rbUseExist.setObjectName("rbUseExist")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.rbUseExist)
        self.rbCreate = QtGui.QRadioButton(EditServerWindow)
        self.rbCreate.setObjectName("rbCreate")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.rbCreate)
        self.rbRSA = QtGui.QRadioButton(EditServerWindow)
        self.rbRSA.setObjectName("rbRSA")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.rbRSA)
        self.lLoginPass = QtGui.QLabel(EditServerWindow)
        self.lLoginPass.setObjectName("lLoginPass")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.lLoginPass)
        self.cbLoginPass = QtGui.QComboBox(EditServerWindow)
        self.cbLoginPass.setObjectName("cbLoginPass")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.cbLoginPass)
        self.lLogin = QtGui.QLabel(EditServerWindow)
        self.lLogin.setObjectName("lLogin")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.lLogin)
        self.leLogin = QtGui.QLineEdit(EditServerWindow)
        self.leLogin.setObjectName("leLogin")
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.leLogin)
        self.lPassword = QtGui.QLabel(EditServerWindow)
        self.lPassword.setObjectName("lPassword")
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.lPassword)
        self.lePassword = QtGui.QLineEdit(EditServerWindow)
        self.lePassword.setObjectName("lePassword")
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.lePassword)
        self.buttonBox = QtGui.QDialogButtonBox(EditServerWindow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.buttonBox)
        self.rbModify = QtGui.QRadioButton(EditServerWindow)
        self.rbModify.setChecked(True)
        self.rbModify.setObjectName("rbModify")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.rbModify)

        self.retranslateUi(EditServerWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), EditServerWindow.close)
        QtCore.QObject.connect(self.rbUseExist, QtCore.SIGNAL("released()"), self.lLoginPass.show)
        QtCore.QObject.connect(self.rbUseExist, QtCore.SIGNAL("released()"), self.cbLoginPass.show)
        QtCore.QObject.connect(self.rbUseExist, QtCore.SIGNAL("released()"), self.lLogin.hide)
        QtCore.QObject.connect(self.rbUseExist, QtCore.SIGNAL("released()"), self.lPassword.hide)
        QtCore.QObject.connect(self.rbUseExist, QtCore.SIGNAL("released()"), self.leLogin.hide)
        QtCore.QObject.connect(self.rbUseExist, QtCore.SIGNAL("released()"), self.lePassword.hide)
        QtCore.QObject.connect(self.rbCreate, QtCore.SIGNAL("released()"), self.lLoginPass.hide)
        QtCore.QObject.connect(self.rbCreate, QtCore.SIGNAL("released()"), self.cbLoginPass.hide)
        QtCore.QObject.connect(self.rbCreate, QtCore.SIGNAL("released()"), self.lLogin.show)
        QtCore.QObject.connect(self.rbCreate, QtCore.SIGNAL("released()"), self.lPassword.show)
        QtCore.QObject.connect(self.rbCreate, QtCore.SIGNAL("released()"), self.leLogin.show)
        QtCore.QObject.connect(self.rbCreate, QtCore.SIGNAL("released()"), self.lePassword.show)
        QtCore.QObject.connect(self.rbRSA, QtCore.SIGNAL("released()"), self.lLoginPass.hide)
        QtCore.QObject.connect(self.rbRSA, QtCore.SIGNAL("released()"), self.cbLoginPass.hide)
        QtCore.QObject.connect(self.rbRSA, QtCore.SIGNAL("released()"), self.lLogin.show)
        QtCore.QObject.connect(self.rbRSA, QtCore.SIGNAL("released()"), self.lPassword.hide)
        QtCore.QObject.connect(self.rbRSA, QtCore.SIGNAL("released()"), self.leLogin.show)
        QtCore.QObject.connect(self.rbRSA, QtCore.SIGNAL("released()"), self.lePassword.hide)
        QtCore.QObject.connect(self.rbModify, QtCore.SIGNAL("released()"), self.lLoginPass.hide)
        QtCore.QObject.connect(self.rbModify, QtCore.SIGNAL("released()"), self.cbLoginPass.hide)
        QtCore.QObject.connect(self.rbModify, QtCore.SIGNAL("released()"), self.lLogin.show)
        QtCore.QObject.connect(self.rbModify, QtCore.SIGNAL("released()"), self.lPassword.show)
        QtCore.QObject.connect(self.rbModify, QtCore.SIGNAL("released()"), self.leLogin.show)
        QtCore.QObject.connect(self.rbModify, QtCore.SIGNAL("released()"), self.lePassword.show)
        QtCore.QMetaObject.connectSlotsByName(EditServerWindow)

    def retranslateUi(self, EditServerWindow):
        EditServerWindow.setWindowTitle(QtGui.QApplication.translate("EditServerWindow", "Modify server configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditServerWindow", "Host (IP or Domain Name) :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditServerWindow", "Port :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("EditServerWindow", "Label for the server :", None, QtGui.QApplication.UnicodeUTF8))
        self.rbUseExist.setText(QtGui.QApplication.translate("EditServerWindow", "Use existing login/password", None, QtGui.QApplication.UnicodeUTF8))
        self.rbCreate.setText(QtGui.QApplication.translate("EditServerWindow", "Use new login/password", None, QtGui.QApplication.UnicodeUTF8))
        self.rbRSA.setText(QtGui.QApplication.translate("EditServerWindow", "Use RSA key", None, QtGui.QApplication.UnicodeUTF8))
        self.lLoginPass.setText(QtGui.QApplication.translate("EditServerWindow", "Login and password to use :", None, QtGui.QApplication.UnicodeUTF8))
        self.lLogin.setText(QtGui.QApplication.translate("EditServerWindow", "Login :", None, QtGui.QApplication.UnicodeUTF8))
        self.lPassword.setText(QtGui.QApplication.translate("EditServerWindow", "Password :", None, QtGui.QApplication.UnicodeUTF8))
        self.rbModify.setText(QtGui.QApplication.translate("EditServerWindow", "Modify current login/password", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc