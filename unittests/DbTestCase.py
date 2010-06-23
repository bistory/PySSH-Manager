# -*- coding: cp1252 -*-
'''
Created on 7 janv. 2010

@author: tle
'''
import unittest
from base.Db import Db

class Test(unittest.TestCase):


    def testConnection(self):
        dblink = Db()
        dblink.close()
        
    """ Vérifie l'intégrité des tables """
    def testIntegrity(self):
        dblink = Db()
        c = dblink.execute("SELECT name,sql FROM sqlite_master WHERE type='table' ORDER BY name")
        
        ok = ""
        for ligne in c:
            if ligne["name"] != "sqlite_sequence":
                ok += " " + ligne["name"]
        
        self.assertEqual(ok, " history servers stored_commands users users_history")
        
        dblink.close()
        
    """ Vérifie que la liste des serveurs est correcte """
    def testServersList(self):
        dblink = Db()
        servers = dblink.getServers()
        
        for ligne in servers:
            print ligne['host']
        
        #self.assertEqual(ok, " history servers stored_commands users users_history")
        
        dblink.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testConnection']
    unittest.main()