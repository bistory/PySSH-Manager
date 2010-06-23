# -*- coding: utf-8 -*-
from PyQt4 import QtCore

from threading import Thread

class Monitor(QtCore.QObject):
    """
    Class created by PyUML

    
    # PyUML: Do not remove this line! # XMI_ID:_sfp70BCnEd-9mr2Tj73dvA

    # PyUML: Associations of this class:
    # PyUML: Association (being 'dst') to class Ssh (being 'src') in package /base/ 
"""

    def __init__(self, server, interval = 5.0):
        super(Monitor, self).__init__()
        
        self.server = server
        self.interval = interval
        
        self.cpuload = 0
        self.mem_used = 0
        self.mem_total = 0
        self.processes = ''
        
        self.cpu_alert = False
        self.mem_alert = False
        
        self.started = False
        self.advanced = False
        
        self.thread = False
        
        self.noresponse = 0
        
        # Avoid blocking the GUI when the server doesn't respond fast enough
        self.hadResponse = True
        
        # Creates the timer but doesn't start it
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL('timeout()'), self.thread_refresh_monitoring)
        
        #self.start()
    
    def __del__(self):
        self.stop()
       
    def stop(self):
        self.timer.stop()
        #self.thread.join()
        self.server.emit_notconnected()
        self.started = False
    
    def start(self):
        if not self.started:
            self.timer.start(5000)
        
    def refresh_monitoring(self):
        if self.server.server.os == 'linux':
            # Get total available memory (only once)
            # Avoid to get it again if already got
            if self.mem_total == 0:
                self.mem_total = int(self.server.sendCommand('free -m|awk \'{if(NR==2) { print $2 }}\'').strip())
            
            self.cpuload, self.mem_used = self.server.sendCommand('ps aux|awk \'NR > 0 { s +=$3 }; END {print s}\' && free -m|awk \'{if(NR==3) { print $3 }}\'').strip().split()
            
            self.cpuload = round(float( self.cpuload.strip() ))
            self.mem_used = int(self.mem_used.strip())
            
            # Fix in certain conditions for the CPU load bar
            if self.cpuload > 100:
                self.cpuload = 100
            
            # Get running processes (only when on advanced monitoring)
            if self.advanced:
                self.processes = self.server.sendCommand('ps -eo pcpu,pid,user,args | sort -k 1 -r').strip()
        
        elif self.server.server.os == 'freebsd':
            # Get total available memory (only once)
            # Avoid to get it again if already got
            if self.mem_total == 0:
                memory = self.server.sendCommand('top -b | grep Mem | awk \'{ print $2, $4, $6, $8, $10, $12 }\'').strip().split()
                for mem in memory:
                    self.mem_total += int( mem[0:(len(mem)-1)] )
            
            self.cpuload = 100 - float(self.server.sendCommand('vmstat cpu 1 2|awk \'{if(NR==4) { print $17 }}\'').strip())
            
            self.mem_used = 0
            memory = self.server.sendCommand('top -b | grep Mem | awk \'{ print $2, $4 }\'').strip().split()
            for mem in memory:
                self.mem_used += int( mem[0:(len(mem)-1)] )
            
            # Get running processes (only when on advanced monitoring)
            if self.advanced:
                self.processes = self.server.sendCommand('ps -axeo pcpu,pid,user,args | sort -k 1 -r').strip()
        
        # Emits signal that values are refreshed
        self.emit(QtCore.SIGNAL('refreshedValues()'))
        # Emits alert if necessary
        self.check_status()
        
        self.hadResponse = True
    
    def check_status(self):
        # CPU load alerts
        if self.cpuload >= 60 and self.cpuload < 80:
            self.emit(QtCore.SIGNAL('cpuWarning'), self.server.server.id)
            self.cpu_alert = True
        elif self.cpuload >= 80 and self.cpuload < 90:
            self.emit(QtCore.SIGNAL('cpuAlert'), self.server.server.id)
            self.cpu_alert = True
        elif self.cpuload >= 90:
            self.emit(QtCore.SIGNAL('cpuCritical'), self.server.server.id)
            self.cpu_alert = True
        else:
            self.emit(QtCore.SIGNAL('cpuOk'), self.server.server.id)
            self.cpu_alert = False
        
        # Memory alerts
        if self.mem_total > 0:
            mem_coeff = self.mem_used / self.mem_total
            if mem_coeff >= 0.6 and mem_coeff < 0.8:
                self.emit(QtCore.SIGNAL('memWarning'), self.server.server.id)
                self.mem_alert = True
            if mem_coeff >= 0.8 and mem_coeff < 0.9:
                self.emit(QtCore.SIGNAL('memAlert'), self.server.server.id)
                self.mem_alert = True
            if mem_coeff >= 0.9:
                self.emit(QtCore.SIGNAL('memCritical'), self.server.server.id)
                self.mem_alert = True
            else:
                self.emit(QtCore.SIGNAL('memOk'), self.server.server.id)
                self.mem_alert = False
        
    def thread_refresh_monitoring(self):
        if self.hadResponse:
            if self.thread:
                self.thread.join()
            if self.server.isConnected:
                self.hadResponse = False
                self.thread = Thread(None, self.refresh_monitoring)
                self.thread.start()
            self.noresponse = 0
        else:
            self.noresponse += 1
            # Stops the monitoring if the server didn't reply (timeout)
            if self.noresponse == 2:
                self.stop()
    
    def set_advanced(self, type = True):
        self.advanced = type
    
    def set_interval(self, interval):
        self.interval = interval

    def memory_load(self):
        """ Created by PyUML """
        return (self.mem_used, self.mem_total)

    def cpu_load(self):
        """ Created by PyUML """
        return self.cpuload

    def processes(self):
        """ Created by PyUML """
        return self.processes
