# -*- coding: utf-8 -*-
'''
Created on 15 janv. 2010

@author: Thomas Lété
'''
import platform, subprocess
from PyQt4 import QtCore, QtGui

from UI_MainWindow import Ui_MainWindow
from MainWindowTab import MainWindowTab
from AddServerWindow import AddServerWindow
from EditServerWindow import EditServerWindow
from EditLoginPassWindow import EditLoginPassWindow
from EditBookmarksWindow import EditBookmarksWindow
from SendCommand import SendCommand
from SendCommandPool import SendCommandPool

from base.Db import Db
from base.ServersPool import ServersPool


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Link to the Db
        self.dblink = Db()
        # Servers pool for basic monitoring
        self.servers = ServersPool()
        
        # List of opened tabs
        self.tabs = {}
        self.servers_items = {}
        self.welcome_tab = True
        
        self.threads = []
        
        # Add connectors to the "Add server" button and menu
        self.connect(self.ui.pbAddServer, QtCore.SIGNAL('clicked()'),
                     self.on_event_pbAddServer_clicked)
        
        self.connect(self.ui.actionAdd_server, QtCore.SIGNAL('triggered()'),
                     self.on_event_pbAddServer_clicked)
        
        # Add connectors to the "Edit server" button
        self.connect(self.ui.pbEditServer, QtCore.SIGNAL('clicked()'),
                     self.on_event_pbEditServer_clicked)
        
        # Add connector to "Delete server" button
        self.connect(self.ui.pbDelServer, QtCore.SIGNAL('clicked()'),
                     self.on_event_pbDelServer_clicked)
        
        # Add connector to "Reconnect to server" button
        self.connect(self.ui.pbRefreshServer, QtCore.SIGNAL('clicked()'),
                     self.on_event_pbRefreshServer_clicked)
        
        # Add connectors to the "Manage logins and passwords" button and menu
        self.connect(self.ui.actionManage_logins_and_passwords, QtCore.SIGNAL('triggered()'),
                     self.on_actionManage_logins_and_passwords_clicked)
        
        # Add connectors to the "Send a command to servers" menu
        self.connect(self.ui.actionSend_a_command_to_servers, QtCore.SIGNAL('triggered()'),
                     self.on_actionSend_a_command_to_servers_clicked)
        
        # Add connectors to the "Manage bookmarks" menu
        self.connect(self.ui.actionManage_bookmarks, QtCore.SIGNAL('triggered()'),
                     self.on_actionManage_bookmarks_clicked)
        
        # Add connectors to the "Read Help" menu
        self.connect(self.ui.actionRead_Help, QtCore.SIGNAL('triggered()'),
                     self.on_actionRead_Help_clicked)
        
        # "About" trigger
        self.connect(self.ui.actionAbout, QtCore.SIGNAL('triggered()'),
                     self.on_actionAbout_clicked)
        
        # Add connector to the servers list
        self.connect(self.ui.lwServers, QtCore.SIGNAL('itemDoubleClicked(QListWidgetItem *)'),
                     self.on_event_lwServers_itemDoubleClicked)
        
        # Add context menu to the servers list
        self.connect(self.ui.lwServers, QtCore.SIGNAL('customContextMenuRequested(const QPoint &)'),
                     self.on_lwservers_contextmenu_requested)
        
        ### BEGIN CONTEXT MENU
        # Add context menu to the servers list
        self.contextMenu = QtGui.QMenu(self.tr('Context menu'), self)
        openAction = self.contextMenu.addAction(self.tr('Open advanced monitoring'))
        sendCommandAction = self.contextMenu.addAction(self.tr('Send a command'))
        openInteractAction = self.contextMenu.addAction(self.tr('Open an interactive shell'))
        editAction = self.contextMenu.addAction(self.tr('Edit'))
        deleteAction = self.contextMenu.addAction(self.tr('Delete'))
        reconnectAction = self.contextMenu.addAction(self.tr('Reconnect'))
        
        # Add connectors
        self.connect(openAction, QtCore.SIGNAL('triggered()'),
                     self.on_contextmenu_openAction_clicked)
        
        # Add connectors
        self.connect(sendCommandAction, QtCore.SIGNAL('triggered()'),
                     self.on_contextmenu_sendCommandAction_clicked)
        
        # Add connectors
        self.connect(openInteractAction, QtCore.SIGNAL('triggered()'),
                     self.on_contextmenu_openInteractAction_clicked)
        
        # Add connectors
        self.connect(editAction, QtCore.SIGNAL('triggered()'),
                     self.on_contextmenu_editAction_clicked)
        
        # Add connectors
        self.connect(deleteAction, QtCore.SIGNAL('triggered()'),
                     self.on_contextmenu_deleteAction_clicked)
        
        # Add connectors
        self.connect(reconnectAction, QtCore.SIGNAL('triggered()'),
                     self.on_contextmenu_reconnectAction_clicked)
        ### END CONTEXT MENU
        
        # Close tab from advanced monitors
        self.connect(self.ui.twMonitor, QtCore.SIGNAL('tabCloseRequested(int)'),
                     self.removeTab)
        
        # "Reduce to tray" trigger
        self.connect(self.ui.actionReduce, QtCore.SIGNAL('triggered()'),
                     self.hide)
        
        # Setup icons
        self.online_icon = QtGui.QIcon()
        self.online_icon.addPixmap(QtGui.QPixmap(':/img/Tick-32.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.offline_icon = QtGui.QIcon()
        self.offline_icon.addPixmap(QtGui.QPixmap(':/img/Notconnected-32.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.offline_icon.addPixmap(QtGui.QPixmap(":/img/Notconnected-32.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        
        self.waiting_icon = QtGui.QIcon()
        self.waiting_icon.addPixmap(QtGui.QPixmap(':/img/Clock-32.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.waiting_icon.addPixmap(QtGui.QPixmap(":/img/Clock-32.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        
        self.warning_icon = QtGui.QIcon()
        self.warning_icon.addPixmap(QtGui.QPixmap(':/img/Warning-32.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.tab_icon = QtGui.QIcon()
        self.tab_icon.addPixmap(QtGui.QPixmap(':/img/Statistics_32.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        # Setup the tray icon
        self.trayIcon = QtGui.QSystemTrayIcon(QtGui.QIcon(':/img/Activity-monitor-32.png'), self)
        menu = QtGui.QMenu(self)
        openAction = menu.addAction(self.tr('Open'))
        closeAction = menu.addAction(self.tr('Reduce to tray'))
        exitAction = menu.addAction(self.tr('Exit'))
        self.trayIcon.setContextMenu(menu)
        self.trayIcon.show()
        
        self.connect(openAction, QtCore.SIGNAL('triggered()'),
                     self.show)
        
        self.connect(closeAction, QtCore.SIGNAL('triggered()'),
                     self.hide)
        
        self.connect(exitAction, QtCore.SIGNAL('triggered()'),
                     self.close)
        
        self.connect(self.trayIcon, QtCore.SIGNAL('activated(QSystemTrayIcon::ActivationReason)'),
                     self.on_iconActivated)
        
        self.connect(self.trayIcon, QtCore.SIGNAL('messageClicked()'),
                     self.on_iconMessageClicked)
        
        # Fill the servers list
        self.fillServersList()
    
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, self.tr('Are you sure ?'), self.tr('Are you sure you really want to quit ?'),
                                   QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        
        if reply == QtGui.QMessageBox.Yes:
            self.hide()
            self.__del__()
            
            # Cleanly close each ssh connection
            try:
                del self.servers
            except:
                pass
            #for server in self.servers:
            #    server.close()
            
            event.accept()
        else:
            event.ignore()
    
    def __del__(self):
        self.trayIcon.hide()
        
    """
    Fills the servers list (GUI) from the Db
    """
    def fillServersList(self):
        dblink = Db()
        self.ui.lwServers.clear()
        servers = dblink.getServers()
        
        i = 0
        for ligne in servers:
            self.addServerToMonitor(ligne)
            i += 1
            
    def addServerToMonitor(self, server):
        if self.servers_items.has_key(server['id']):
            self.servers_items[server['id']].setIcon(self.waiting_icon)
            self.servers_items[server['id']].setToolTip(self.tr('Waiting for connection...'))
            self.servers_items[server['id']].setText(server['type'])
            
            self.servers_items[server['id']].setStatusTip(self.tr('Host') + ' : ' + server['host'] + ':' + str(server['port']) + '    ' + self.tr('Login') + ' : ' + server['login'])
            
            if server['login'] == '' and server['password'] == '':
                print 'rsa'
                self.servers.edit(server['id'], server['host'], server['port'], server['type'], 'rsa', 'rsa')
            else:
                self.servers.edit(server['id'], server['host'], server['port'], server['type'], server['login'], server['password'])
            
            # Connects
            self.connect(self.servers[server['id']], QtCore.SIGNAL('connected'),
                         self.on_server_connected)
            self.connect(self.servers[server['id']], QtCore.SIGNAL('notConnected'),
                         self.on_server_notConnected)
            
            self.servers_items[server['id']].setIcon(self.waiting_icon)
            
            # Reconnects to the server
            self.servers[server['id']].connect()
        else:
            item = QtGui.QListWidgetItem(self.ui.lwServers)
            item.setData(32, QtCore.QVariant(server['id']))
            item.setIcon(self.waiting_icon)
            item.setToolTip(self.tr('Waiting for connection...'))
            item.setText(server['type'])
            
            item.setStatusTip(self.tr('Host') + ' : ' + server['host'] + ':' + str(server['port']) + '    ' + self.tr('Login') + ' : ' + server['login'])
            
            self.servers.add(server['id'], server['host'], server['port'], server['type'], server['login'], server['password'])
            
            self.servers_items[server['id']] = item
            
            # Connects
            self.connect(self.servers[server['id']], QtCore.SIGNAL('connected'),
                         self.on_server_connected)
            self.connect(self.servers[server['id']], QtCore.SIGNAL('notConnected'),
                         self.on_server_notConnected)
            
            self.servers_items[server['id']].setIcon(self.waiting_icon)
            self.servers[server['id']].connect()
    
    def list_servers_get_selected_id(self):
        server_id, trash = self.ui.lwServers.currentItem().data(32).toInt()
        
        return server_id
        
    """
    SLOTS
    """
    # Opens the "Add Server" window
    def on_event_pbAddServer_clicked(self):
        addServerWindow = AddServerWindow(self.dblink, self)
        addServerWindow.show()
    
    # Opens the "Edit Server" window
    def on_event_pbEditServer_clicked(self):
        server_id = self.list_servers_get_selected_id()
        
        editServerWindow = EditServerWindow(self.dblink, self.servers[server_id], server_id, self)
        editServerWindow.show()
    
    # Delete a server from the db
    def on_event_pbDelServer_clicked(self):
        reply = QtGui.QMessageBox.question(self, self.tr('Are you sure ?'), self.tr('Are you sure you really want to delete this server ?'),
                                   QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        
        if reply == QtGui.QMessageBox.Yes:
            # Get the ID of the server (id is the same as the one in DB)
            server_id = self.list_servers_get_selected_id()
            self.ui.lwServers.takeItem(self.ui.lwServers.currentRow())
            
            if self.servers.has_key(server_id):
                del self.servers[server_id]
                
            if self.servers_items.has_key(server_id):
                del self.servers_items[server_id]
                
            if self.tabs.has_key(server_id):
                del self.tabs[server_id]
                
            self.dblink.removeServer(server_id)
        
    def on_event_pbRefreshServer_clicked(self):
        # Get the ID of the server (id is the same as the one in DB)
        server_id = self.list_servers_get_selected_id()
        
        self.servers[server_id].connect()
        
        self.servers_items[server_id].setIcon(self.waiting_icon)
    
    # Opens the "Edit Server" window
    def on_actionManage_logins_and_passwords_clicked(self):
        editLoginPassWindow = EditLoginPassWindow(self.dblink, self)
        editLoginPassWindow.show()
    
    # Opens the "Edit Server" window
    def on_actionSend_a_command_to_servers_clicked(self):
        sendCommandPool = SendCommandPool(self.dblink, self.servers, self)
        sendCommandPool.show()
       
    def on_actionManage_bookmarks_clicked(self):
        editBookmarksWindow = EditBookmarksWindow(self.dblink, self)
        editBookmarksWindow.show()
    
    def on_actionRead_Help_clicked(self):
        if platform.system() == 'Linux':
            subprocess.Popen('/usr/bin/xdg-open ../doc/userguide.pdf', shell=True)
        elif platform.system() == 'Darwin':
            subprocess.Popen('/usr/bin/open ../doc/userguide.pdf', shell=True)
        elif platform.system() == 'Windows':
            subprocess.Popen('start ..\doc\userguide.pdf', shell=True)
    
    def on_actionAbout_clicked(self):
        splash = QtGui.QSplashScreen(self, QtGui.QPixmap(':/img/splash.png'))
        splash.show()
        splash.showMessage('v 1.0', QtCore.Qt.AlignRight, QtCore.Qt.white)

    # Opens a new tab with advanced monitoring for the double-clicked server in the list
    def on_event_lwServers_itemDoubleClicked(self, item):
        # Get server id from defined data
        id = self.list_servers_get_selected_id()
        
        # Check if the ssh server is online
        if self.servers[id].isConnected:
            # Check if a tab doesn't already exist
            # If it exists, switch to the tab
            if self.tabs.has_key(id):
                self.ui.twMonitor.setCurrentWidget(self.tabs[id])
            # Doesn't exist, create a new tab
            else:
                # Close the welcome tab
                if self.welcome_tab:
                    self.ui.twMonitor.clear()
                    self.welcome_tab = False
                
                # Create a tab and store the object
                tab = MainWindowTab(self.dblink, self.servers[id])
                tab.setId(id)
                self.tabs[id] = tab
                self.ui.twMonitor.addTab(tab, self.tab_icon, item.text())
                
                # Switch to the current tab
                self.ui.twMonitor.setCurrentWidget(tab)
        else:
            self.on_event_pbRefreshServer_clicked()
            
    def removeTab(self, tab_id):
        if not self.welcome_tab or tab_id != 0:
            id = self.ui.twMonitor.widget(tab_id).getId()
        
            # Delete the tab from the GUI
            self.ui.twMonitor.removeTab(tab_id)
            
            # Delete the tab object
            self.tabs[id].stop()
            del self.tabs[id]
        else:
            self.welcome_tab = False
            
            # Delete the tab from the GUI
            self.ui.twMonitor.removeTab(tab_id)
        
        # Reopen the welcome tab if no tab remain
        if not self.welcome_tab and self.ui.twMonitor.count() == 0:
            self.ui.twMonitor.clear()
            self.welcome_tab = True
            self.ui.twMonitor.addTab(self.ui.welcome_tab, self.tab_icon, self.tr('Welcome'))
    
    # Monitoring events
    # CPU
    def on_cpuOk(self, server_id):
        # Sets online icon
        if not self.servers[server_id].monitoring.mem_alert:
            self.servers_items[server_id].setIcon(self.online_icon)
        
    def on_cpuWarning(self, server_id):
        self.trayIcon.showMessage(self.tr('Warning !'), self.tr('Server ') + self.servers[server_id].server.type + self.tr(' has more than 60% CPU load !'))
        # Sets warning icon
        self.servers_items[server_id].setIcon(self.warning_icon)
        
    def on_cpuAlert(self, server_id):
        self.trayIcon.showMessage(self.tr('Alert !'), self.tr('Server ') + self.servers[server_id].server.type + self.tr(' has more than 80% CPU load !'), QtGui.QSystemTrayIcon.Warning)
        # Sets warning icon
        self.servers_items[server_id].setIcon(self.warning_icon)
        
    def on_cpuCritical(self, server_id):
        self.trayIcon.showMessage(self.tr('Critical !'), self.tr('Server ') + self.servers[server_id].server.type + self.tr(' has more than 90% CPU load !'), QtGui.QSystemTrayIcon.Critical)
        # Sets warning icon
        self.servers_items[server_id].setIcon(self.warning_icon)
        
    # Memory
    def on_memOk(self, server_id):
        # Sets online icon
        if not self.servers[server_id].monitoring.cpu_alert:
            self.servers_items[server_id].setIcon(self.online_icon)
        
    def on_memWarning(self, server_id):
        self.trayIcon.showMessage(self.tr('Warning !'), self.tr('Server ') + self.servers[server_id].server.type + self.tr(' has more than 60% memory used !'))
        # Sets warning icon
        self.servers_items[server_id].setIcon(self.warning_icon)
        
    def on_memAlert(self, server_id):
        self.trayIcon.showMessage(self.tr('Alert !'), self.tr('Server ') + self.servers[server_id].server.type + self.tr(' has more than 80% memory used !'), QtGui.QSystemTrayIcon.Warning)
        # Sets warning icon
        self.servers_items[server_id].setIcon(self.warning_icon)
        
    def on_memCritical(self, server_id):
        self.trayIcon.showMessage(self.tr('Critical !'), self.tr('Server ') + self.servers[server_id].server.type + self.tr(' has more than 90% memory used !'), QtGui.QSystemTrayIcon.Critical)
        # Sets warning icon
        self.servers_items[server_id].setIcon(self.warning_icon)
        
    def on_iconActivated(self, reason):
        if reason == QtGui.QSystemTrayIcon.Trigger:
            self.raise_()
            if self.isVisible():
                self.hide()
            else:
                self.show()
        
    def on_iconMessageClicked(self):
        self.show()
    
    def on_server_connected(self, server):
        self.servers_items[server.server.id].setToolTip(self.tr('Online'))
        self.servers_items[server.server.id].setIcon(self.online_icon)
        self.servers[server.server.id].monitor()
        
        self.servers_items[server.server.id].setStatusTip(self.tr('Host') + ' : ' + str(server.server.hostname) + ' (' + server.server.host + ':' + str(server.server.port) + ')    ' + self.tr('Login') + ' : ' + server.auth.login)
        
        # Connect to the monitoring signals (warnings, alerts, criticals)
        # CPU
        self.connect(server.monitoring, QtCore.SIGNAL('cpuOk'),
                     self.on_cpuOk)
        #self.connect(server.monitoring, QtCore.SIGNAL('cpuWarning'),
        #             self.on_cpuWarning)
        self.connect(server.monitoring, QtCore.SIGNAL('cpuAlert'),
                     self.on_cpuAlert)
        self.connect(server.monitoring, QtCore.SIGNAL('cpuCritical'),
                     self.on_cpuCritical)
        # Memory
        self.connect(server.monitoring, QtCore.SIGNAL('memOk'),
                     self.on_memOk)
        #self.connect(server.monitoring, QtCore.SIGNAL('memWarning'),
        #             self.on_memWarning)
        self.connect(server.monitoring, QtCore.SIGNAL('memAlert'),
                     self.on_memAlert)
        self.connect(server.monitoring, QtCore.SIGNAL('memCritical'),
                     self.on_memCritical)
    
    def on_server_notConnected(self, server):
        self.servers_items[server.server.id].setToolTip(self.tr('Offline'))
        self.servers_items[server.server.id].setIcon(self.offline_icon)
    
    def on_lwservers_contextmenu_requested(self, pos):
        pos.setX(pos.x() + 10)
        pos.setY(pos.y() + 40)
        self.contextMenu.exec_(self.mapToGlobal(pos))
    
    def on_contextmenu_openAction_clicked(self):
        self.on_event_lwServers_itemDoubleClicked(self.ui.lwServers.currentItem())
    
    def on_contextmenu_sendCommandAction_clicked(self):
        server_id = self.list_servers_get_selected_id()
        
        self.sendCommand = SendCommand(self.dblink, self.servers[server_id], self)
        self.sendCommand.show()
    
    def on_contextmenu_openInteractAction_clicked(self):
        server_id = self.list_servers_get_selected_id()
        
        self.servers[server_id].open_interactive_shell()
    
    def on_contextmenu_editAction_clicked(self):
        self.on_event_pbEditServer_clicked()
    
    def on_contextmenu_deleteAction_clicked(self):
        self.on_event_pbDelServer_clicked()
    
    def on_contextmenu_reconnectAction_clicked(self):
        self.on_event_pbRefreshServer_clicked()