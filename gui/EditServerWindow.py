# -*- coding: utf-8 -*-
'''
Created on 25 janv. 2010

@author: Thomas Lété
'''
from PyQt4 import QtCore, QtGui

from UI_EditServerWindow import Ui_EditServerWindow

class EditServerWindow(QtGui.QDialog):
    def __init__(self, dblink, server, id, parent=None):
        super(EditServerWindow, self).__init__(parent)
        self.parent = parent
        
        self.ui = Ui_EditServerWindow()
        self.ui.setupUi(self)
        
        self.dblink = dblink
        
        # Get all the server informations from db
        self.server = self.dblink.getServer(id)
        
        self.ui.leHost.setText(self.server['host'])
        self.ui.sbPort.setValue(self.server['port'])
        self.ui.leLabel.setText(self.server['type'])
        
        self.ui.leLogin.setText(self.server['login'])
        if self.server['password'] != 'rsa':
            self.ui.lePassword.setText(self.server['password'])
        else:
            self.ui.rbRSA.setChecked(True)
            #self.ui.leLogin.hide()
            self.ui.lePassword.hide()
            #self.ui.lLogin.hide()
            self.ui.lPassword.hide()
        
        self.ui.lLoginPass.hide()
        self.ui.cbLoginPass.hide()
        
        self.connect(self.ui.buttonBox, QtCore.SIGNAL('accepted()'),
                     self.accept)
        
        #self.connect(self.ui.rbModify, QtCore.SIGNAL('released()'),
        #             self.accept)
        
        # Fill the login/pass combobox
        auths = self.dblink.getAuths()
        for auth in auths:
            if auth['id'] != self.server['defaultlogin_id']:
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
            else:
                # Get a user id already defined
                user_id, trash = self.ui.cbLoginPass.itemData(self.ui.cbLoginPass.currentIndex()).toInt()
                
            if self.ui.rbModify.isChecked():
                # Edit the old login/pass
                user_id = self.server['defaultlogin_id']
                self.dblink.editUser(self.server['defaultlogin_id'], self.ui.leLogin.text(), self.ui.lePassword.text())
                
            if self.ui.rbRSA.isChecked():
                auth_id, = self.dblink.getDefaultLoginIdByServer(self.server['id'])
                auth = self.dblink.getAuthById(auth_id)
                if auth['password'] == 'rsa':
                    self.dblink.editUser(auth_id, self.ui.leLogin.text(), 'rsa')
                    user_id = auth_id
                # Create a new user and get his id
                else:
                    user_id = self.dblink.addUser(self.ui.leLogin.text(), 'rsa')
                self.ui.lePassword.setText('rsa')
                
            self.dblink.editServer(self.server['id'], self.ui.leHost.text(), self.ui.sbPort.text(), self.ui.leLabel.text(), user_id)
            
            # Add server to monitoring
            server = {
                      'id': self.server['id'],
                      'host': str(self.ui.leHost.text()),
                      'port': int(self.ui.sbPort.text()),
                      'login': str(self.ui.leLogin.text()),
                      'password': str(self.ui.lePassword.text()),
                      'type': str(self.ui.leLabel.text())
                      }
            
            self.parent.addServerToMonitor(server)
            self.close()