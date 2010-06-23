# -*- coding: utf-8 -*-
'''
Created on 15 janv. 2010

@author: Thomas Lété
'''

import re
from PyQt4 import QtCore, QtGui
from base.Ssh import Ssh

from UI_SendCommand import Ui_SendCommand
from ServerResponse import ServerResponse

class SendCommand(QtGui.QDialog):
    def __init__(self, dblink, server, parent=None):
        super(SendCommand, self).__init__(parent)
        self.ui = Ui_SendCommand()
        self.ui.setupUi(self)
        
        self.dblink = dblink
        self.server = server
        self.parent = parent
        
        bookmarks = self.dblink.getBookmarks()
        
        self.ui.bookmarks.clear()
        for bookmark in bookmarks:
            self.ui.bookmarks.addItem(bookmark['label'], QtCore.QVariant(bookmark['command']))
        self.ui.bookmarks.setCurrentIndex(-1)
        
        # Add connector to the combobox of bookmarks
        self.connect(self.ui.bookmarks, QtCore.SIGNAL('currentIndexChanged(int)'),
                     self.on_event_bookmarks_currentIndexChanged)
        
        auths = self.dblink.getAuths()
        self.default_id, = self.dblink.getDefaultLoginIdByServer(server.server.id)
        
        i = 0
        self.ui.cbLoginPass.clear()
        for auth in auths:
            self.ui.cbLoginPass.addItem(auth['login'] + '/' + auth['password'], QtCore.QVariant(auth['id']))
            
            if self.default_id == auth['id']:
                self.ui.cbLoginPass.setCurrentIndex(i)
            i += 1
        
    def accept(self):
        print re.search('rm', self.ui.pteCommand.toPlainText())
        #re.compile('rm ([\-a-zA-Z]+)f').match(self.ui.pteCommand.toPlainText(), 1):
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
            # Change server's auth if needed
            auth_id, trash = self.ui.cbLoginPass.itemData(self.ui.cbLoginPass.currentIndex()).toInt()
            
            if self.default_id != auth_id:
                login, password = self.dblink.getAuthById(auth_id)
                self.server = Ssh(self.server.server.host, self.server.server.port, self.server.server.type, self.server.server.id)
                self.server.set_auth(login, password)
            
            self.hide()
            serverResponse = ServerResponse(self.dblink, self.server, self.ui.pteCommand.toPlainText(), self, self.parent)
            serverResponse.show()
    
    # Modify the contents of the command, thanks to a bookmark
    def on_event_bookmarks_currentIndexChanged(self, index):
        index, trash = QtCore.QVariant(index).toInt()
        text = self.ui.bookmarks.itemData(index).toString()
        self.ui.pteCommand.setPlainText(text)