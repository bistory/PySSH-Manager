# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../src/gui/MainWindow_PROD.ui'
#
# Created: Mon Apr 12 11:59:54 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Activity-monitor-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lwServers = QtGui.QListWidget(self.centralwidget)
        self.lwServers.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lwServers.setMouseTracking(True)
        self.lwServers.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.lwServers.setObjectName("lwServers")
        self.verticalLayout_3.addWidget(self.lwServers)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbAddServer = QtGui.QPushButton(self.centralwidget)
        self.pbAddServer.setMaximumSize(QtCore.QSize(50, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/Plus-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAddServer.setIcon(icon1)
        self.pbAddServer.setObjectName("pbAddServer")
        self.horizontalLayout.addWidget(self.pbAddServer)
        self.pbDelServer = QtGui.QPushButton(self.centralwidget)
        self.pbDelServer.setMaximumSize(QtCore.QSize(50, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/Cross-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbDelServer.setIcon(icon2)
        self.pbDelServer.setObjectName("pbDelServer")
        self.horizontalLayout.addWidget(self.pbDelServer)
        self.pbEditServer = QtGui.QPushButton(self.centralwidget)
        self.pbEditServer.setMaximumSize(QtCore.QSize(50, 16777215))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/Pencil-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbEditServer.setIcon(icon3)
        self.pbEditServer.setObjectName("pbEditServer")
        self.horizontalLayout.addWidget(self.pbEditServer)
        self.pbRefreshServer = QtGui.QPushButton(self.centralwidget)
        self.pbRefreshServer.setMaximumSize(QtCore.QSize(50, 16777215))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/Refresh-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbRefreshServer.setIcon(icon4)
        self.pbRefreshServer.setObjectName("pbRefreshServer")
        self.horizontalLayout.addWidget(self.pbRefreshServer)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.twMonitor = QtGui.QTabWidget(self.centralwidget)
        self.twMonitor.setDocumentMode(True)
        self.twMonitor.setTabsClosable(True)
        self.twMonitor.setMovable(True)
        self.twMonitor.setObjectName("twMonitor")
        self.welcome_tab = QtGui.QWidget()
        self.welcome_tab.setObjectName("welcome_tab")
        self.verticalLayout = QtGui.QVBoxLayout(self.welcome_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.welcome_tab)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/Statistics_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twMonitor.addTab(self.welcome_tab, icon5, "")
        self.horizontalLayout_2.addWidget(self.twMonitor)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuServers = QtGui.QMenu(self.menubar)
        self.menuServers.setObjectName("menuServers")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAdd_server = QtGui.QAction(MainWindow)
        self.actionAdd_server.setObjectName("actionAdd_server")
        self.actionManage_logins_and_passwords = QtGui.QAction(MainWindow)
        self.actionManage_logins_and_passwords.setObjectName("actionManage_logins_and_passwords")
        self.actionReduce = QtGui.QAction(MainWindow)
        self.actionReduce.setObjectName("actionReduce")
        self.actionRead_Help = QtGui.QAction(MainWindow)
        self.actionRead_Help.setObjectName("actionRead_Help")
        self.actionSend_a_command_to_servers = QtGui.QAction(MainWindow)
        self.actionSend_a_command_to_servers.setObjectName("actionSend_a_command_to_servers")
        self.actionManage_bookmarks = QtGui.QAction(MainWindow)
        self.actionManage_bookmarks.setObjectName("actionManage_bookmarks")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionReduce)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuServers.addAction(self.actionAdd_server)
        self.menuServers.addAction(self.actionSend_a_command_to_servers)
        self.menuServers.addAction(self.actionManage_logins_and_passwords)
        self.menuServers.addAction(self.actionManage_bookmarks)
        self.menuAbout.addAction(self.actionRead_Help)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuServers.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.twMonitor.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PySSH Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.pbAddServer.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a new server", None, QtGui.QApplication.UnicodeUTF8))
        self.pbDelServer.setToolTip(QtGui.QApplication.translate("MainWindow", "Delete the selected server", None, QtGui.QApplication.UnicodeUTF8))
        self.pbEditServer.setToolTip(QtGui.QApplication.translate("MainWindow", "Edit the selected server", None, QtGui.QApplication.UnicodeUTF8))
        self.pbRefreshServer.setToolTip(QtGui.QApplication.translate("MainWindow", "Reconnect the selected server", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Welcome to PySSH Monitor !</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose a server <span style=\" font-weight:600;\">on the left</span> and double-click on it to access to advanced monitoring.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Access to different options via the menu.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can keep it running in background by reducing the application.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">If it is the first time you launch this application</span>, you should go to the \"Servers\" menu, to \"Manage logins and passwords\" and modify them to yours if needed.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.twMonitor.setTabText(self.twMonitor.indexOf(self.welcome_tab), QtGui.QApplication.translate("MainWindow", "Welcome", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuServers.setTitle(QtGui.QApplication.translate("MainWindow", "Servers", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_server.setText(QtGui.QApplication.translate("MainWindow", "&Add Server", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_server.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManage_logins_and_passwords.setText(QtGui.QApplication.translate("MainWindow", "&Manage logins and passwords", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManage_logins_and_passwords.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+M", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReduce.setText(QtGui.QApplication.translate("MainWindow", "&Reduce to system tray", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReduce.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRead_Help.setText(QtGui.QApplication.translate("MainWindow", "Read &Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRead_Help.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+H", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSend_a_command_to_servers.setText(QtGui.QApplication.translate("MainWindow", "&Send a command to servers", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSend_a_command_to_servers.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManage_bookmarks.setText(QtGui.QApplication.translate("MainWindow", "Manage bookmarks", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc