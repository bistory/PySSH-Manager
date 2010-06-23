# -*- coding: utf-8 -*-
'''
Created on 15 janv. 2010

@author: Thomas Lété
'''
import re
from PyQt4 import QtCore, QtGui
from base.ServersPool import ServersPool

from ServerResponsePool import ServerResponsePool
from UI_SendCommandPool import Ui_SendCommandPool

class SendCommandPool(QtGui.QDialog):
    def __init__(self, dblink, servers, parent=None):
        super(SendCommandPool, self).__init__(parent)
        self.ui = Ui_SendCommandPool()
        self.ui.setupUi(self)
        
        self.dblink = dblink
        self.servers = servers
        self.parent = parent
        
        self.ui.checkboxes = {}
        self.ui.labels = {}
        self.ui.comboboxes = {}
        
        i = 0
        self.servers.rewind()
        for k, v in servers:
            self.ui.checkboxes[k] = QtGui.QCheckBox(self)
            self.ui.checkboxes[k].setChecked(True)
            self.ui.checkboxes[k].setText(v.server.type)
            self.ui.glServers.addWidget(self.ui.checkboxes[k], i, 0, 1, 1)
            self.ui.comboboxes[k] = QtGui.QComboBox(self)
            self.ui.glServers.addWidget(self.ui.comboboxes[k], i, 1, 1, 1)
            
            # Fill the login/pass combobox
            self.dblink = dblink
            auths = self.dblink.getAuths()
            
            y = 0
            for auth in auths:
                self.ui.comboboxes[k].addItem(auth['login'] + '/' + auth['password'], QtCore.QVariant(auth['id']))
                
                def_id = self.dblink.getDefaultLoginIdByServer(k)
                if auth['id'] == def_id['defaultlogin_id']:
                    self.ui.comboboxes[k].setCurrentIndex(y)
                y += 1
            i += 1
        
        bookmarks = self.dblink.getBookmarks()
        
        self.ui.bookmarks.clear()
        for bookmark in bookmarks:
            self.ui.bookmarks.addItem(bookmark['label'], QtCore.QVariant(bookmark['command']))
        self.ui.bookmarks.setCurrentIndex(-1)
        
        # Add connector to the combobox of bookmarks
        self.connect(self.ui.bookmarks, QtCore.SIGNAL('currentIndexChanged(int)'),
                     self.on_event_bookmarks_currentIndexChanged)
        
    def accept(self):
        # Checks if all the fields have been filed
        if self.ui.pteCommand.toPlainText() == '':
            QtGui.QMessageBox.information(self,
                        self.tr('Information'),
                        self.tr('You must enter a command.'))
        elif re.search('rm [\-a-zA-Z]+f', self.ui.pteCommand.toPlainText()):
            QtGui.QMessageBox.information(self,
                        self.tr('Information'),
                        self.tr('You must not use dangerous commands.'))
        else:
            self.servers.rewind()
            servers = ServersPool()
            
            for k, v in self.servers:
                if self.ui.checkboxes[k].isChecked():
                    #servers[k] = self.servers[k]
                    id, trash = self.ui.comboboxes[k].itemData(self.ui.comboboxes[k].currentIndex()).toInt()
                    login, password = self.dblink.getAuthById(id)
                    
                    servers.add(k, self.servers[k].server.host, self.servers[k].server.port, self.servers[k].server.type, login, password)
            
            self.hide()
            serverResponse = ServerResponsePool(self.dblink, servers, self.ui.pteCommand.toPlainText(), self, self.parent)
            serverResponse.show()
    
    # Modify the contents of the command, thanks to a bookmark
    def on_event_bookmarks_currentIndexChanged(self, index):
        index, trash = QtCore.QVariant(index).toInt()
        text = self.ui.bookmarks.itemData(index).toString()
        self.ui.pteCommand.setPlainText(text)