# -*- coding: utf-8 -*-
'''
Created on 15 janv. 2010

@author: Thomas Lété
'''

from PyQt4 import QtCore, QtGui
from threading import Thread

from UI_ServerResponse import Ui_ServerResponse
from BookmarkCommandWindow import BookmarkCommandWindow

class ServerResponse(QtGui.QDialog):
    def __init__(self, dblink, server, command, previous=None, parent=None):
        super(ServerResponse, self).__init__(parent)
        self.ui = Ui_ServerResponse()
        self.ui.setupUi(self)
        
        self.previous = previous
        self.parent = parent
        self.dblink = dblink
        self.server = server
        self.command = command
        
        self.ui.response.setPlainText(self.tr('Waiting for response ...'))
        
        # Connect the slots for thread-safety
        self.connect(self, QtCore.SIGNAL('commandResult()'),
                     self.commandResult)
        
        # Add connector to "Send an other command"
        self.connect(self.ui.pbSendAnOtherCommand, QtCore.SIGNAL('clicked()'),
                     self.on_event_pbSendAnOtherCommand_clicked)
        
        # Fills the command reminder
        self.ui.pteCommandReminder.setPlainText(self.command)
        
        # Start a thread to execute the monitoring refresh (without blocking the GUI)
        self.t = Thread(None, self.sendCommand)
        self.t.start()
        
    def sendCommand(self):
        if not self.server.isConnected:
            self.server.connect()
        self.result = self.server.sendCommand(self.command)
        
        if self.result == '':
            self.result = self.tr('(Empty results)')
        
        if self.result == False:
            self.result = self.tr('An error occured')
        
        self.emit(QtCore.SIGNAL('commandResult()'))
        
    def commandResult(self):
        self.ui.response.setPlainText(self.result)
        
    def accept(self):
        if self.ui.bookmark.isChecked():
            bookmarkCommandWindow = BookmarkCommandWindow(self.dblink, self.command, self.parent)
            bookmarkCommandWindow.show()
            
        self.close()
    
    def on_event_pbSendAnOtherCommand_clicked(self):
        self.previous.show()
        self.close()