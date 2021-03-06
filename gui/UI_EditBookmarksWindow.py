# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../src/gui/EditBookmarksWindow.ui'
#
# Created: Mon Apr 12 12:00:01 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditBookmarksWindow(object):
    def setupUi(self, EditBookmarksWindow):
        EditBookmarksWindow.setObjectName("EditBookmarksWindow")
        EditBookmarksWindow.setWindowModality(QtCore.Qt.WindowModal)
        EditBookmarksWindow.resize(700, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Bookmark_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditBookmarksWindow.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(EditBookmarksWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lwBookmarks = QtGui.QListWidget(EditBookmarksWindow)
        self.lwBookmarks.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lwBookmarks.setObjectName("lwBookmarks")
        self.verticalLayout.addWidget(self.lwBookmarks)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pbAddBookmark = QtGui.QPushButton(EditBookmarksWindow)
        self.pbAddBookmark.setMaximumSize(QtCore.QSize(50, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/Plus-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAddBookmark.setIcon(icon1)
        self.pbAddBookmark.setObjectName("pbAddBookmark")
        self.horizontalLayout_2.addWidget(self.pbAddBookmark)
        self.pbDelBookmark = QtGui.QPushButton(EditBookmarksWindow)
        self.pbDelBookmark.setMaximumSize(QtCore.QSize(50, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/Cross-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbDelBookmark.setIcon(icon2)
        self.pbDelBookmark.setObjectName("pbDelBookmark")
        self.horizontalLayout_2.addWidget(self.pbDelBookmark)
        self.pbImport = QtGui.QPushButton(EditBookmarksWindow)
        self.pbImport.setMaximumSize(QtCore.QSize(50, 16777215))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/Down_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbImport.setIcon(icon3)
        self.pbImport.setObjectName("pbImport")
        self.horizontalLayout_2.addWidget(self.pbImport)
        self.pbExport = QtGui.QPushButton(EditBookmarksWindow)
        self.pbExport.setMaximumSize(QtCore.QSize(50, 16777215))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/Up-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbExport.setIcon(icon4)
        self.pbExport.setObjectName("pbExport")
        self.horizontalLayout_2.addWidget(self.pbExport)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.GroupBox = QtGui.QGroupBox(EditBookmarksWindow)
        self.GroupBox.setObjectName("GroupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.GroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.GroupBox)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pteCommand = QtGui.QPlainTextEdit(self.GroupBox)
        self.pteCommand.setObjectName("pteCommand")
        self.verticalLayout_2.addWidget(self.pteCommand)
        self.label_2 = QtGui.QLabel(self.GroupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.pteDescription = QtGui.QPlainTextEdit(self.GroupBox)
        self.pteDescription.setObjectName("pteDescription")
        self.verticalLayout_2.addWidget(self.pteDescription)
        self.buttonBox = QtGui.QDialogButtonBox(self.GroupBox)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout.addWidget(self.GroupBox)

        self.retranslateUi(EditBookmarksWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), EditBookmarksWindow.close)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), EditBookmarksWindow.accept)
        QtCore.QMetaObject.connectSlotsByName(EditBookmarksWindow)

    def retranslateUi(self, EditBookmarksWindow):
        EditBookmarksWindow.setWindowTitle(QtGui.QApplication.translate("EditBookmarksWindow", "Manage bookmarks", None, QtGui.QApplication.UnicodeUTF8))
        self.pbAddBookmark.setToolTip(QtGui.QApplication.translate("EditBookmarksWindow", "Add a new bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.pbDelBookmark.setToolTip(QtGui.QApplication.translate("EditBookmarksWindow", "Delete the selected bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.pbImport.setToolTip(QtGui.QApplication.translate("EditBookmarksWindow", "Import bookmarks", None, QtGui.QApplication.UnicodeUTF8))
        self.pbExport.setToolTip(QtGui.QApplication.translate("EditBookmarksWindow", "Export bookmarks", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox.setTitle(QtGui.QApplication.translate("EditBookmarksWindow", "Edit bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EditBookmarksWindow", "Command :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EditBookmarksWindow", "Description :", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc
