# -*- coding: utf-8 -*-
'''
Created on 1 feb. 2010

@author: Thomas Lété
'''
import pickle
from PyQt4 import QtCore, QtGui

from UI_EditBookmarksWindow import Ui_EditBookmarksWindow
from AddBookmarkWindow import AddBookmarkWindow

class EditBookmarksWindow(QtGui.QDialog):
    def __init__(self, dblink, parent=None):
        super(EditBookmarksWindow, self).__init__(parent)
        self.ui = Ui_EditBookmarksWindow()
        self.ui.setupUi(self)
        
        # Add connector to "Delete bookmark" button
        self.connect(self.ui.pbAddBookmark, QtCore.SIGNAL('clicked()'),
                     self.on_event_pbAddBookmark_clicked)
        
        # Add connector to "Delete bookmark" button
        self.connect(self.ui.pbDelBookmark, QtCore.SIGNAL('clicked()'),
                     self.on_event_pbDelBookmark_clicked)
        
        # Add connector to "Delete bookmark" button
        self.connect(self.ui.pbImport, QtCore.SIGNAL('clicked()'),
                     self.on_event_pbImport_clicked)
        
        # Add connector to "Delete bookmark" button
        self.connect(self.ui.pbExport, QtCore.SIGNAL('clicked()'),
                     self.on_event_pbExport_clicked)
        
        # Add connector to the servers list
        self.connect(self.ui.lwBookmarks, QtCore.SIGNAL('currentItemChanged(QListWidgetItem *, QListWidgetItem *)'),
                     self.on_event_lwBookmarks_currentItemChanged)
        
        self.ui.lwBookmarks.clear()
        
        self.dblink = dblink
        
        self.bookmarks_items = {}
        
        self.fillBookmarksList()
    
    # Fill the list of bookmarks
    def fillBookmarksList(self):
        self.ui.lwBookmarks.clear()
        bookmarks = self.dblink.getBookmarks()
        
        for bookmark in bookmarks:
            item = QtGui.QListWidgetItem()
            item.setData(32, QtCore.QVariant(bookmark['id']))
            item.setToolTip(self.tr('Click to edit'))
            item.setText(bookmark['label'])
            
            self.ui.lwBookmarks.addItem(item)
            
            self.bookmarks_items[bookmark['id']] = item

    # Opens edit mode
    def on_event_lwBookmarks_currentItemChanged(self, item, previous):
        # Get server id from defined data
        try:
            id, trash = item.data(32).toInt()
            bookmark = self.dblink.getBookmarkById(str(id))
            
            self.ui.pteCommand.setPlainText(bookmark['command'])
            self.ui.pteDescription.setPlainText(bookmark['label'])
        except:
            pass
    
    # Delete a bookmark from the db
    def on_event_pbDelBookmark_clicked(self):
        # Get the ID of the server (id is the same as the one in DB)
        row = self.ui.lwBookmarks.row(self.ui.lwBookmarks.currentItem())
        id, trash = self.ui.lwBookmarks.currentItem().data(32).toInt()
        
        self.dblink.removeBookmark(id)
        
        self.ui.pteCommand.setPlainText('')
        self.ui.pteDescription.setPlainText('')
        
        # DIRTY HACK TO REMOVE AN ITEM
        self.fillBookmarksList()
        
        try:
            self.ui.lwBookmarks.setCurrentRow(row)
        except:
            pass
    
    # Delete a bookmark from the db
    def on_event_pbAddBookmark_clicked(self):
        addBookmarkWindow = AddBookmarkWindow(self.dblink, self)
        addBookmarkWindow.show()
    
    # Accept the changes to the item
    def accept(self):
        command = self.ui.pteCommand.toPlainText()
        description = self.ui.pteDescription.toPlainText()
        
        # Checks if all the fields have been filed
        if command == '' and description == '':
            self.close()
        else:
            # Checks if all the fields have been filed
            if command == '' or description == '':
                QtGui.QMessageBox.information(self,
                            self.tr('Information'),
                            self.tr('You must fill all the required fields.'))
            else:
                # Get the ID of the server (id is the same as the one in DB)
                id, trash = self.ui.lwBookmarks.currentItem().data(32).toInt()
                
                self.dblink.editBookmark(id, command, description)
                
                # DIRTY HACK TO EDIT AN ITEM
                self.fillBookmarksList()
    
    def on_event_pbImport_clicked(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, self.tr('Import bookmarks'), '', self.tr('Bookmark files (*.bkm)'))
        
        if filename != '':
            f = open(filename, 'r')
            bookmarks = pickle.load(f)
            #filedata = f.read()
            f.close()
            
            reply = QtGui.QMessageBox.question(self, self.tr('Are you sure ?'), self.tr('Do you want to import ') + str(len(bookmarks)) + (' bookmarks ?'),
                               QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            
            if reply == QtGui.QMessageBox.Yes:
                for bookmark in bookmarks:
                    self.dblink.addBookmark(bookmark[1], bookmark[0])
        
            # DIRTY HACK TO REMOVE AN ITEM
            self.fillBookmarksList()
       
    def on_event_pbExport_clicked(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, self.tr('Export bookmarks'), 'bookmarks.bkm', self.tr('Bookmark files (*.bkm)'))
        
        if filename != '':
            obj = []
            bookmarks = self.dblink.getBookmarks()
            
            for bookmark in bookmarks:
                obj.append([bookmark['label'], bookmark['command']])
            
            f = open(filename, 'w')
            pickle.dump(obj, f)
            f.close()