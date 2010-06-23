# -*- coding: utf-8 -*-
import os

class Auth:
    """
    Class created by PyUML
    # PyUML: Do not remove this line! # XMI_ID:_9UZZcfqwEd6nNqLO14QYJA

    # PyUML: Associations of this class:
    # PyUML: Association (being 'src') to class Ssh (being 'dst') in package /base/ 
"""

    def __init__(self, login, password = 'rsa'):
        """ Created by PyUML """
        self.dblink = None  # created by PyUML
        self.login = login  # created by PyUML
        self.password = password  # created by PyUML

    def is_rsa(self):
        return self.password == 'rsa'
    
    def get_rsa_files(self):
        path = '../ssh'
        dir = os.listdir(path)
        
        out = []
        for file in dir:
            out.append(path + '/' + file)
        
        return out