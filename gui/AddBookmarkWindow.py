# -*- coding: utf-8 -*-
'''
Created on 1 feb. 2010

@author: Thomas Lété
'''
from PyQt4 import QtCore, QtGui

from UI_AddBookmarkWindow import Ui_AddBookmarkWindow

class AddBookmarkWindow(QtGui.QDialog):
    def __init__(self, dblink, parent=None):
        super(AddBookmarkWindow, self).__init__(parent)
        self.ui = Ui_AddBookmarkWindow()
        self.ui.setupUi(self)
        
        self.dblink = dblink
        self.parent = parent
        
    def accept(self):
        # Checks if all the fields have been filed
        if self.ui.pteCommand.toPlainText() == '' or self.ui.pteDescription.toPlainText() == '':
            QtGui.QMessageBox.information(self,
                        self.tr('Information'),
                        self.tr('You must fill all the required fields.'))
        else:
            self.dblink.addBookmark(self.ui.pteCommand.toPlainText(), self.ui.pteDescription.toPlainText())
            self.parent.fillBookmarksList()
            
            self.close()