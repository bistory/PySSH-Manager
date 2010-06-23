# -*- coding: utf-8 -*-
'''
Created on 15 janv. 2010

@author: Thomas Lété
'''
from PyQt4 import QtCore, QtGui
from threading import Thread

from UI_ServerResponsePool import Ui_ServerResponsePool
from ServerResponsePoolView import ServerResponsePoolView
from BookmarkCommandWindow import BookmarkCommandWindow

class ServerResponsePool(QtGui.QDialog):
    def __init__(self, dblink, servers, command, previous=None, parent=None):
        super(ServerResponsePool, self).__init__(parent)
        self.ui = Ui_ServerResponsePool()
        self.ui.setupUi(self)
        
        self.previous = previous
        self.parent = parent
        self.dblink = dblink
        
        self.ok_icon = QtGui.QPixmap(':/img/Tick-32.png')
        self.nok_icon = QtGui.QPixmap(':/img/Cross-32.png')
        
        self.command = command
        self.servers = servers
        
        self.responses = {}
        self.ui.serverNames = {}
        self.ui.showResponses = {}
        self.ui.pbCopies = {}
        self.ui.spacerItems = {}
        self.ui.spacerItems1 = {}
        self.ui.serverStatus = {}
        self.serverResponsePoolView = {}
        self.threads = []
        
        # Connect the slots for thread-safety
        self.connect(self, QtCore.SIGNAL('connected'),
                     self.connected)
        self.connect(self, QtCore.SIGNAL('notConnected'),
                     self.notConnected)
        
        # Add connector to "Send an other command"
        self.connect(self.ui.pbSendAnOtherCommand, QtCore.SIGNAL('clicked()'),
                     self.on_event_pbSendAnOtherCommand_clicked)
        
        # Fills the command reminder
        self.ui.pteCommandReminder.setPlainText(self.command)
        
        i = 0
        for k, server in self.servers:
            # Server name (label)
            self.ui.serverNames[k] = QtGui.QLabel(self)
            font = QtGui.QFont()
            font.setWeight(75)
            font.setBold(True)
            self.ui.serverNames[k].setFont(font)
            self.ui.serverNames[k].setText(server.server.type)
            self.ui.gridLayout.addWidget(self.ui.serverNames[k], i, 0, 1, 1)
            
            # First separator
            self.ui.spacerItems[k] = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            self.ui.gridLayout.addItem(self.ui.spacerItems[k], i, 1, 1, 1)
            
            # Clock
            self.ui.serverStatus[k] = QtGui.QLabel(self)
            self.ui.serverStatus[k].setPixmap(QtGui.QPixmap(':/img/Clock-32.png'))
            self.ui.serverStatus[k].setAlignment(QtCore.Qt.AlignCenter)
            self.ui.gridLayout.addWidget(self.ui.serverStatus[k], i, 2, 1, 1)
            
            # Second separator
            self.ui.spacerItems1[k] = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            self.ui.gridLayout.addItem(self.ui.spacerItems1[k], i, 3, 1, 1)
            
            # Copy push button
            self.ui.pbCopies[k] = QtGui.QPushButton(self)
            self.ui.pbCopies[k].setToolTip(self.tr('Copy response to clipboard.'))
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(':/img/copy.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.pbCopies[k].setIcon(icon2)
            self.ui.pbCopies[k].setDisabled(True)
            self.ui.gridLayout.addWidget(self.ui.pbCopies[k], i, 4, 1, 1)
            
            # View response push button
            self.ui.showResponses[k] = QtGui.QPushButton(self)
            self.ui.showResponses[k].setText(self.tr('View the server response'))
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(':/img/find.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.showResponses[k].setIcon(icon1)
            self.ui.showResponses[k].setDisabled(True)
            self.ui.gridLayout.addWidget(self.ui.showResponses[k], i, 5, 1, 1)
            
            # Connect to a response view
            self.serverResponsePoolView[k] = ServerResponsePoolView(self.parent)
            self.connect(self.ui.showResponses[k], QtCore.SIGNAL('clicked()'),
                     self.serverResponsePoolView[k].show)
            
            # Connect to a copy button
            self.connect(self.ui.pbCopies[k], QtCore.SIGNAL('clicked()'),
                     self.serverResponsePoolView[k].copyToClipboard)
            
            # Default response string
            self.responses[k] = 'Waiting for response ...'
            
            t = Thread(None, self.sendCommand, None, [k])
            t.daemon = True
            t.start()
            self.threads.append(t)
            
            i += 1
            
        # Join the threads
        self.t = Thread(None, self.joinThreads)
        #self.t.daemon = True
        self.t.start()
        
    def sendCommand(self, server_key):
        # Trying to connect
        if not self.servers[server_key].isConnected:
            self.servers[server_key].connect_thread()
        
        self.responses[server_key] = self.servers[server_key].sendCommand(self.command)
        
        if self.responses[server_key] == '':
            self.responses[server_key] = self.tr('(Empty results)')
        
        if self.responses[server_key] != False:
            self.serverResponsePoolView[server_key].response = self.responses[server_key]
            
            self.emit(QtCore.SIGNAL('connected'), (server_key))
        else:
            if not self.servers[server_key].isConnected:
                self.serverResponsePoolView[server_key].response = self.tr('Unable to connect')
            self.emit(QtCore.SIGNAL('notConnected'), (server_key))
    
    def joinThreads(self):
        for t in self.threads:
            t.join()
    
    def connected(self, server_key):
        self.ui.serverStatus[server_key].setPixmap(self.ok_icon)
        self.ui.pbCopies[server_key].setEnabled(True)
        self.ui.showResponses[server_key].setEnabled(True)
    
    def notConnected(self, server_key):
        self.ui.serverStatus[server_key].setPixmap(self.nok_icon)
        
    def accept(self):
        if self.ui.bookmark.isChecked():
            bookmarkCommandWindow = BookmarkCommandWindow(self.dblink, self.command, self.parent)
            bookmarkCommandWindow.show()
            
        self.close()
    
    def on_event_pbSendAnOtherCommand_clicked(self):
        self.previous.show()
        self.close()