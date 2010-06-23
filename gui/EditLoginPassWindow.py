# -*- coding: utf-8 -*-
'''
Created on 27 janv. 2010

@author: Thomas Lété
'''
from PyQt4 import QtCore, QtGui

from UI_EditLoginPassWindow import Ui_EditLoginPassWindow
from AddUserWindow import AddUserWindow

class EditLoginPassWindow(QtGui.QDialog):
    def __init__(self, dblink, parent=None):
        super(EditLoginPassWindow, self).__init__(parent)
        self.ui = Ui_EditLoginPassWindow()
        self.ui.setupUi(self)
        
        # Add connector to "Delete user" button
        self.connect(self.ui.pbAddPair, QtCore.SIGNAL('clicked()'),
                     self.on_event_pbAddPair_clicked)
        
        # Add connector to "Delete user" button
        self.connect(self.ui.pbDelPair, QtCore.SIGNAL('clicked()'),
                     self.on_event_pbDelPair_clicked)
        
        # Add connector to the servers list
        self.connect(self.ui.lwLoginPass, QtCore.SIGNAL('currentItemChanged(QListWidgetItem *,QListWidgetItem *)'),
                     self.on_event_lwLoginPass_currentItemChanged)
        
        self.ui.lwLoginPass.clear()
        
        self.dblink = dblink
        
        self.auths_items = {}
        
        self.fillUsersList()
    
    # Fill the list of login/passwords
    def fillUsersList(self):
        self.ui.lwLoginPass.clear()
        auths = self.dblink.getAuths()
        
        for auth in auths:
            item = QtGui.QListWidgetItem(self.ui.lwLoginPass)
            item.setData(32, QtCore.QVariant(auth['id']))
            item.setToolTip(self.tr('Click to edit'))
            item.setText(auth['login'] + '/' + auth['password'])
            
            self.auths_items[auth['id']] = item

    # Opens a new tab with advanced monitoring for the double-clicked server in the list
    def on_event_lwLoginPass_currentItemChanged(self, item, previous):
        # Get server id from defined data
        id, trash = item.data(32).toInt()
        auth = self.dblink.getAuthById(str(id))
        
        self.ui.leLogin.setText(auth['login'])
        self.ui.lePassword.setText(auth['password'])
        
        self.ui.lwDefault.clear()
        servers = self.dblink.getServersByDefaultId(id)
        for server in servers:
            self.ui.lwDefault.addItem(server['type'])
    
    # Delete a server from the db
    def on_event_pbDelPair_clicked(self):
        # Get the ID of the server (id is the same as the one in DB)
        user_id, trash = self.ui.lwLoginPass.currentItem().data(32).toInt()
        
        self.dblink.removeUser(user_id)
        
        self.ui.leLogin.setText('')
        self.ui.lePassword.setText('')
        
        # DIRTY HACK TO REMOVE AN ITEM
        self.fillUsersList()
    
    # Delete a server from the db
    def on_event_pbAddPair_clicked(self):
        addUserWindow = AddUserWindow(self.dblink, self)
        addUserWindow.show()
        
    def accept(self):
        # Checks if all the fields have been filed
        if self.ui.leLogin.text() == '' or self.ui.lePassword.text() == '':
            QtGui.QMessageBox.information(self,
                        self.tr('Information'),
                        self.tr('You must fill all the required fields.'))
        else:
            login = self.ui.leLogin.text()
            password = self.ui.lePassword.text()
            
            if login != '' and password != '':
                # Get the ID of the server (id is the same as the one in DB)
                user_id, trash = self.ui.lwLoginPass.currentItem().data(32).toInt()
                
                self.dblink.editUser(user_id, login, self.ui.lePassword.text())
                
                # DIRTY HACK TO EDIT AN ITEM
                self.fillUsersList()
            else:
                self.close()