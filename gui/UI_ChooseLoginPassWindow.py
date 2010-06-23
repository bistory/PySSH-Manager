# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../src/gui/ChooseLoginPassWindow.ui'
#
# Created: Mon Apr 12 11:59:59 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ChooseLoginPassWindow(object):
    def setupUi(self, ChooseLoginPassWindow):
        ChooseLoginPassWindow.setObjectName("ChooseLoginPassWindow")
        ChooseLoginPassWindow.setWindowModality(QtCore.Qt.WindowModal)
        ChooseLoginPassWindow.resize(640, 125)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/User_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ChooseLoginPassWindow.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(ChooseLoginPassWindow)
        self.gridLayout.setObjectName("gridLayout")

        self.retranslateUi(ChooseLoginPassWindow)
        QtCore.QMetaObject.connectSlotsByName(ChooseLoginPassWindow)

    def retranslateUi(self, ChooseLoginPassWindow):
        ChooseLoginPassWindow.setWindowTitle(QtGui.QApplication.translate("ChooseLoginPassWindow", "Choose login an passes to use", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc
