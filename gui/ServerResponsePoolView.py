# -*- coding: utf-8 -*-
'''
Created on 15 janv. 2010

@author: Thomas Lété
'''
# On importe les classes principales de Qt
from PyQt4 import QtCore, QtGui

# On importe la classe auto-générée par pyuic
from UI_ServerResponsePoolView import Ui_ServerResponsePoolView

# On crée la classe d'interface et on hérite du bon type d'interface
# (QDialog, QWidget, etc...)
class ServerResponsePoolView(QtGui.QDialog):
    def __init__(self, parent=None):
        # On construit l'objet en invoquant le constructeur de sa superclasse
        super(ServerResponsePoolView, self).__init__(parent)
        # On construit l'interface générée dans Qt Designer
        self.ui = Ui_ServerResponsePoolView()
        # On installe l'interface sur l'actuelle et on la dessine
        self.ui.setupUi(self)
        
        self.response = self.tr('Waiting for response ...')
        
    def show(self):
        self.ui.response.setPlainText(self.response)
        super(ServerResponsePoolView, self).show()
    
    def copyToClipboard(self):
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(self.response)