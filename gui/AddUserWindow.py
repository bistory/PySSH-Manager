# -*- coding: utf-8 -*-
'''
Created on 27 janv. 2010

@author: Thomas Lété
'''
from PyQt4 import QtCore, QtGui

from UI_AddUserWindow import Ui_AddUserWindow

class AddUserWindow(QtGui.QDialog):
    def __init__(self, dblink, parent=None):
        super(AddUserWindow, self).__init__(parent)
        self.ui = Ui_AddUserWindow()
        self.ui.setupUi(self)
        
        self.dblink = dblink
        self.parent = parent
        
    def accept(self):
        # Checks if all the fields have been filed
        if self.ui.leLogin.text() == '' or self.ui.lePassword.text() == '':
            QtGui.QMessageBox.information(self,
                        self.tr('Information'),
                        self.tr('You must fill all the required fields.'))
        else:
            self.dblink.addUser(self.ui.leLogin.text(), self.ui.lePassword.text())
            self.parent.fillUsersList()
            
            self.close()