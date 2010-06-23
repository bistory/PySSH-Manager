# -*- coding: utf-8 -*-
'''
Created on 15 janv. 2010

@author: Thomas Lété
'''
from PyQt4 import QtCore, QtGui

from UI_ChooseLoginPassWindow import Ui_ChooseLoginPassWindow
from ServerResponsePool import ServerResponsePool

class ChooseLoginPassWindow(QtGui.QDialog):
    def __init__(self, dblink, servers, command, parent=None):
        super(ChooseLoginPassWindow, self).__init__(parent)
        self.ui = Ui_ChooseLoginPassWindow()
        self.ui.setupUi(self)
        
        self.dblink = dblink
        self.parent = parent
        
        #self.ui.items = {}
        self.ui.checkboxes = {}
        self.ui.labels = {}
        self.ui.comboboxes = {}
        
        i = 0
        servers.rewind()
        for k, v in servers:
            self.ui.checkboxes[k] = QtGui.QCheckBox(self)
            self.ui.checkboxes[k].setChecked(True)
            self.ui.checkboxes[k].setText(v.server.type)
            self.ui.gridLayout.addWidget(self.ui.checkboxes[k], i, 0, 1, 1)
            self.ui.comboboxes[k] = QtGui.QComboBox(self)
            self.ui.gridLayout.addWidget(self.ui.comboboxes[k], i, 1, 1, 1)
            
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
            
        self.ui.buttonBox = QtGui.QDialogButtonBox(self)
        self.ui.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.ui.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.ui.gridLayout.addWidget(self.ui.buttonBox, i, 1, 1, 1)

        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
        
    def accept(self):
        self.hide()
        serverResponse = ServerResponsePool(self.servers, self.command, self.parent)
        serverResponse.show()