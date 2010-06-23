# -*- coding: utf-8 -*-
'''
Created on 15 janv. 2010

@author: Thomas Lété
'''
from PyQt4 import QtCore, QtGui

from UI_BookmarkCommandWindow import Ui_BookmarkCommandWindow

class BookmarkCommandWindow(QtGui.QDialog):
    def __init__(self, dblink, command, parent=None):
        super(BookmarkCommandWindow, self).__init__(parent)
        self.ui = Ui_BookmarkCommandWindow()
        self.ui.setupUi(self)
        
        self.dblink = dblink
        self.command = command
        
        self.ui.command.setPlainText(command)
        
    def accept(self):
        # Checks if all the fields have been filed
        if self.ui.description.toPlainText() == '' or self.ui.command.toPlainText() == '':
            QtGui.QMessageBox.information(self,
                        self.tr('Information'),
                        self.tr('You must fill all the required fields.'))
        else:
            self.dblink.addBookmark(self.ui.command.toPlainText(), self.ui.description.toPlainText())
            self.close()