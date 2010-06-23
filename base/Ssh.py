# -*- coding: utf-8 -*-
from PyQt4 import QtCore

import platform, paramiko, subprocess, os
from threading import Timer

from Server import Server
from Auth import Auth
from Monitor import Monitor

connectDelay = .1

class Ssh(QtCore.QObject):
    """
    Class created by PyUML

    
    # PyUML: Do not remove this line! # XMI_ID:_sfuNQBCnEd-9mr2Tj73dvA

    # PyUML: Associations of this class:
    # PyUML: Association (being 'src') to class ServersPool (being 'dst') in package /base/ 
    # PyUML: Association (being 'dst') to class Server (being 'src') in package /base/ 
    # PyUML: Association (being 'dst') to class Auth (being 'src') in package /base/ 
    # PyUML: Association (being 'src') to class Monitor (being 'dst') in package /base/ 
"""
    server = None  # created by PyUML

    def __init__(self, host, port, type, id = 0):
        super(Ssh, self).__init__()
        
        self.auth = None  # created by PyUML
        self.server = Server(host, port, type, id)
        
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.isConnected = False
        
        self.monitoring = Monitor(self)
    
    def __del__(self):
        self.close()
        
    def set_auth(self, login, password = 'rsa'):
        self.auth = Auth(login, password)
    
    def connect_thread(self):
        try:
            if self.auth.is_rsa():
                self.client.connect(self.server.host, self.server.port, self.auth.login, key_filename=self.auth.get_rsa_files(), timeout=25)
            else:
                self.client.connect(self.server.host, self.server.port, self.auth.login, self.auth.password, timeout=25)
            self.isConnected = self.client.get_transport().is_active()
            
            if(self.isConnected):
                self.client.get_transport().set_keepalive(300)
            
            hostname, os = self.sendCommand('hostname && uname').split()
            self.server.set_hostname(hostname)
            self.server.set_os(os.lower())
            
            # Emits signal that server is connected
            self.emit(QtCore.SIGNAL('connected'), self)
            
            return True
        
        except:
            # Emits signal that server is connected
            self.emit_notconnected()
            #self.emit(QtCore.SIGNAL('notConnected'), self)
            
            print 'Unable to connect to %s:%s with login %s, pass %s' % (self.server.host, self.server.port, self.auth.login, self.auth.password)
            QtCore.QCoreApplication.processEvents();
            
            try:
                self.client.close()
            except:
                pass
            return False

    def connect(self):
        try:
            self.close()
        finally:
            # Connect to the servers (thread-safe)
            # Random avoid to fail a connection on windows when all connections
            # are initialized
            global connectDelay
            t = Timer(connectDelay, self.connect_thread)
            t.start()
            connectDelay += .1

    def close(self):
        self.client.close()
        if self.isConnected:
            # Emits signal that server is connected
            self.emit_notconnected()
        self.isConnected = False
        #self.emit(QtCore.SIGNAL('notConnected'), self)

    def sendCommand(self, command):
        if self.isConnected:
            if not self.client.get_transport().is_active():
                self.isConnected = False
                # Emits signal that server is connected
                self.emit_notconnected()
                #self.emit(QtCore.SIGNAL('notConnected'), self)
            
            stdin, stdout, stderr = self.client.exec_command(command)
            response = stdout.read()
            
            if response == False:
                return stderr.read()
            else:
                return response
        else:
            return False
    
    def sendInteractiveCommand(self, command, args):
        if self.isConnected:
            i = 0
            stdin, stdout, stderr = self.client.exec_command(command)
            while stdout.channel.closed is False:
                stdin.write('%s\n' % args[i])
                stdin.flush()
                ++i
            # Reinitialize sudo
            self.sendCommand('sudo -k')
            response = stdout.read()
            
            if response == False:
                return stderr.read()
            else:
                return response
        else:
            return False
    
    def monitor(self, interval = 5.0):
        self.monitoring.set_interval(interval)
        self.monitoring.start()
    
    def open_interactive_shell(self):
        if platform.system() == 'Linux':
            try:
                # Gnome
                subprocess.Popen('gnome-terminal -e "ssh ' + self.server.host + ' -p ' + str(self.server.port) + ' -l ' + str(self.auth.login) + '"', shell=True)
                
            except:
                # KDE
                try:
                    subprocess.Popen('konsole -e "ssh ' + self.server.host + ' -p ' + str(self.server.port) + ' -l ' + str(self.auth.login) + '"', shell=True)
                except:
                    print 'No terminal found'
            
        elif platform.system() == 'Darwin':
            subprocess.Popen('/bin/sh base/term.sh /usr/bin/ssh ' + self.server.host + ' -p ' + str(self.server.port) + ' -l ' + str(self.auth.login), shell=True)
            #try:
            #    # Mac OSX
            #    subprocess.Popen('open -n -a /Applications/Utilities/Terminal.app /usr/bin/ssh ' + self.server.host + ' -p ' + str(self.server.port) + ' -l ' + str(self.auth.login), shell=True)
            #except:
            #    print 'No terminal found'
            
        elif platform.system() == 'Windows':
            # Windows
            try:
                subprocess.Popen('putty.exe -ssh -2 -P ' + str(self.server.port) + ' ' + str(self.auth.login) + '@' + self.server.host + ' -pw ' + str(self.auth.password), shell=True)
            except:
                print 'No terminal found'
    
    def emit_notconnected(self):
        self.emit(QtCore.SIGNAL('notConnected'), self)
