# -*- coding: utf-8 -*-
'''
Created on 15 janv. 2010

@author: Thomas Lété
'''
from PyQt4 import QtCore, QtGui

from UI_AddServerWindow import Ui_AddServerWindow

class AddServerWindow(QtGui.QDialog):
    def __init__(self, dblink, parent=None):
        super(AddServerWindow, self).__init__(parent)
        self.ui = Ui_AddServerWindow()
        self.ui.setupUi(self)
        
        self.ui.lLogin.hide()
        self.ui.lPassword.hide()
        self.ui.leLogin.hide()
        self.ui.lePassword.hide()
        
        self.connect(self.ui.buttonBox, QtCore.SIGNAL('accepted()'),
                     self.accept)
        
        self.parent = parent
        
        # Fill the login/pass combobox
        self.dblink = dblink
        auths = self.dblink.getAuths()
        for auth in auths:
            self.ui.cbLoginPass.addItem(auth['login'] + '/' + auth['password'], QtCore.QVariant(auth['id']))
        
        
    def accept(self):
        # Checks if all the fields have been filed
        if self.ui.leHost.text() == '' or self.ui.sbPort.text() == 0 or (self.ui.rbCreate.isChecked() and (self.ui.leLogin.text() == '' or self.ui.lePassword.text() == '')) or (self.ui.rbRSA.isChecked() and self.ui.leLogin.text() == '') or self.ui.leLabel.text() == '':
            QtGui.QMessageBox.information(self,
                        self.tr('Information'),
                        self.tr('You must fill all the required fields.'))
        else:
            if self.ui.rbCreate.isChecked():
                # Create a new user and get his id
                user_id = self.dblink.addUser(self.ui.leLogin.text(), self.ui.lePassword.text())
            elif self.ui.rbRSA.isChecked():
                user_id = self.dblink.addUser(self.ui.leLogin.text(), 'rsa')
                self.ui.lePassword.setText('rsa')
            else:
                # Get a user id already defined
                user_id, trash = self.ui.cbLoginPass.itemData(self.ui.cbLoginPass.currentIndex()).toInt()
                auth = self.dblink.getAuthById(user_id)
                self.ui.leLogin.setText(auth['login'])
                self.ui.lePassword.setText(auth['password'])
            
            server_id = self.dblink.addServer(self.ui.leHost.text(), self.ui.sbPort.text(), self.ui.leLabel.text(), user_id)
            
            # Add server to monitoring
            server = {
                      'id': server_id,
                      'host': str(self.ui.leHost.text()),
                      'port': int(self.ui.sbPort.text()),
                      'login': str(self.ui.leLogin.text()),
                      'password': str(self.ui.lePassword.text()),
                      'type': str(self.ui.leLabel.text())
                      }
            
            self.parent.addServerToMonitor(server)
            self.close()