# -*- coding: utf-8 -*-
'''
Created on 19 janv. 2010

@author: Thomas Lété
'''
from PyQt4 import QtCore, QtGui

from SendCommand import SendCommand

class MainWindowTab(QtGui.QWidget):
    '''
    classdocs
    '''

    def __init__(self, dblink, server, parent=None):
        '''
        Constructor
        '''
        super(MainWindowTab, self).__init__(parent)
        
        self.dblink = dblink
        self.server = server
        
        self.advancedGuiLoaded = False
        
        # ID of the server
        self.id = 0
        
        verticalLayout = QtGui.QVBoxLayout(self)
        self.pbMonitorLoad = QtGui.QProgressBar(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbMonitorLoad.sizePolicy().hasHeightForWidth())
        self.pbMonitorLoad.setSizePolicy(sizePolicy)
        self.pbMonitorLoad.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbMonitorLoad.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pbMonitorLoad.setMaximum(0)
        self.pbMonitorLoad.setProperty('value', QtCore.QVariant(-1))
        self.pbMonitorLoad.setAlignment(QtCore.Qt.AlignCenter)
        self.pbMonitorLoad.setOrientation(QtCore.Qt.Horizontal)
        self.pbMonitorLoad.setInvertedAppearance(False)
        verticalLayout.addWidget(self.pbMonitorLoad)
        
        self.server.monitor()
        self.server.monitoring.set_advanced()
        self.server.monitoring.thread_refresh_monitoring()
        # Connect the slots for thread-safety
        self.connect(self.server.monitoring, QtCore.SIGNAL('refreshedValues()'),
                     self.refreshedValues)
    
    def __del__(self):
        self.stop()
    
    def stop(self):
        self.server.monitoring.set_advanced(False)
        
    def setupAdvancedMonitor(self):
        self.pbMonitorLoad.hide()
        verticalLayout = self.layout()
        verticalLayout.removeItem(verticalLayout.itemAt(0))
        gridLayout = QtGui.QGridLayout()
        self.pbOpenShell = QtGui.QPushButton(self)
        self.pbOpenShell.setText(self.tr('Open an interactive shell'))
        gridLayout.addWidget(self.pbOpenShell, 0, 1, 1, 1)
        self.pbRefresh = QtGui.QPushButton(self)
        self.pbRefresh.setText(self.tr('Refresh Monitoring'))
        gridLayout.addWidget(self.pbRefresh, 0, 2, 1, 1)
        self.pbSendCommand = QtGui.QPushButton(self)
        self.pbSendCommand.setText(self.tr('Send a command') + ' ...')
        gridLayout.addWidget(self.pbSendCommand, 0, 0, 1, 1)
        verticalLayout.addLayout(gridLayout)
        gridLayout = QtGui.QGridLayout()
        label = QtGui.QLabel(self)
        label.setText(self.tr('CPU Load') + ' :')
        label.setMinimumSize(QtCore.QSize(250, 0))
        gridLayout.addWidget(label, 0, 0, 1, 1)
        label = QtGui.QLabel(self)
        label.setText(self.tr('Memory Occupation') + ' :')
        gridLayout.addWidget(label, 1, 0, 1, 1)
        self.pbMemory = QtGui.QProgressBar(self)
        self.pbMemory.setMaximumSize(QtCore.QSize(16777215, 14))
        self.pbMemory.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(self.pbMemory, 1, 1, 1, 1)
        self.pbCpuLoad = QtGui.QProgressBar(self)
        self.pbCpuLoad.setMaximumSize(QtCore.QSize(16777215, 14))
        self.pbCpuLoad.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(self.pbCpuLoad, 0, 1, 1, 1)
        verticalLayout.addLayout(gridLayout)
        label = QtGui.QLabel(self)
        label.setText(self.tr('Running Processes') + ' :')
        verticalLayout.addWidget(label)
        self.teProcesses = QtGui.QTextEdit(self)
        font = QtGui.QFont()
        font.setFamily('Courier New')
        self.teProcesses.setFont(font)
        verticalLayout.addWidget(self.teProcesses)
        
        # Add connectors
        self.connect(self.pbRefresh, QtCore.SIGNAL('clicked()'),
                     self.server.monitoring.refresh_monitoring)
        self.connect(self.pbSendCommand, QtCore.SIGNAL('clicked()'),
                     self.on_event_pbSendCommand_clicked)
        self.connect(self.pbOpenShell, QtCore.SIGNAL('clicked()'),
                     self.on_event_pbOpenShell_clicked)
        
        self.advancedGuiLoaded = True
    
    def setMonitorValues(self, cpuload, mem_used, mem_total, process):
        self.pbMemory.setMaximum(mem_total)
        self.pbMemory.setProperty('value', QtCore.QVariant(mem_used))
        self.pbMemory.setToolTip(str(mem_used) + self.tr('Mb') + ' / ' + str(mem_total) + self.tr('Mb'))
        
        self.pbCpuLoad.setProperty('value', QtCore.QVariant(cpuload))
        self.teProcesses.setText(process)
    
    def refreshedValues(self):
        if not self.advancedGuiLoaded:
            self.setupAdvancedMonitor()
        
        self.setMonitorValues(self.server.monitoring.cpuload, self.server.monitoring.mem_used, self.server.monitoring.mem_total, self.server.monitoring.processes)
        
    def setId(self, id):
        self.id = id
        
    def getId(self):
        return self.id
        
    """
    SLOTS
    """
    def on_event_pbSendCommand_clicked(self):
        self.sendCommand = SendCommand(self.dblink, self.server, self)
        self.sendCommand.show()
        
    def on_event_pbOpenShell_clicked(self):
        self.server.open_interactive_shell()