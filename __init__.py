# -*- coding: utf-8 -*-
'''
Created on 20 janv. 2010

@author: Thomas Lété
'''

import sys
sys.stdout = open('pyssh_stdout.log', 'w')
sys.stderr = open('pyssh_stderr.log', 'w')

from PyQt4 import QtGui

from gui.MainWindow import MainWindow

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    
    myapp = MainWindow()
    myapp.show()
    myapp.raise_()
    sys.exit(app.exec_())